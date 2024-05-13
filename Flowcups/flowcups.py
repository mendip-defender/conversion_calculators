# -*- coding: utf-8 -*-
""" These equations convert cup drain time, collected at 25 °C and between the minimum and maximum drain times indicated, into kinematic viscosity values in mm²/s (cSt).
    Based on the data provided in the following standards, ASTM D4212, ASTM D1200, DIN 53211 and ISO 2341.

    Copyright © 2024-05 Jack Stringer https://github.com/mendip-defender/"""

import numpy as np

def Zahn_Cup(cup,t):
    """Convert the cup drain time (t) into kinematic viscosity values in mm²/s (cSt) for Zahn Cups
    Following the data from ASTM D4212 X3.3 and table X3.1
    State Cup number followed by the time for example:
    Zahn Cup #2 with a drain time of 35 seconds
    Zahn_Cup(1,35)
    This should give you a reading of 73.5 mm²/s (cSt)
    
    Equation is V = K(t−c)
    | Type  | Cup Number | Drain Time | Orifice | Recommended Oil Viscosity |   K   |  c   |
    |-------|------------|------------|---------|---------------------------|-------|------|
    | Zahn  |          1 | 35 to 80   | 2.0 mm  | 20 mm²/s (cSt)            |   1.1 |   29 |
    | Zahn  |          2 | 20 to 80   | 2.7 mm  | 120 mm²/s (cSt)           |   3.5 |   14 |
    | Zahn  |          3 | 20 to 80   | 3.8 mm  | 480 mm²/s (cSt)           |  11.7 |  7.5 |
    | Zahn  |          4 | 20 to 80   | 4.3 mm  | 480 mm²/s (cSt)           |  14.8 |    5 |
    | Zahn  |          5 | 20 to 80   | 5.3 mm  | 900 or 1600 mm²/s (cSt)   |    23 |    0 |"""
    if cup == 1:
        K = 1.1
        c = 29
    elif cup == 2:
        K = 3.5
        c = 14
    elif cup == 3:
        K = 11.7
        c = 7.5
    elif cup == 4:
        K = 14.8
        c = 5
    elif cup == 5:
        K = 23
        c = 0
    else:
        K = 1.1
        c = 29

    return K * (t - c)

def Shell_Cup(cup,t):
    """Convert the cup drain time (t) into kinematic viscosity values in mm²/s (cSt) for Shell Cups
    Following the data from ASTM D4212
    State Cup number followed by the time for example:
    Shell Cup #2.5 with a drain time of 55 seconds
    Shell_Cup(2.5,55)
    This should give you a reading of 28.35 mm²/s (cSt)
    
    Equation is V = K(t−c)
    
    | Type  | Cup Number | Drain Time | Orifice | Recommended Oil Viscosity |   K   |  c   |
    |-------|------------|------------|---------|---------------------------|-------|------|
    | Shell |          1 | 20 to 80   | 1.8 mm  | 9 mm²/s (cSt)             | 0.226 |   13 |
    | Shell |          2 | 20 to 80   | 2.4 mm  | 9 or 20 mm²/s (cSt)       | 0.576 |    5 |
    | Shell |        2.5 | 20 to 80   | 2.7 mm  | 35 mm²/s (cSt)            | 0.925 |    3 |
    | Shell |          3 | 20 to 80   | 3.1 mm  | 35 or 120 mm²/s (cSt)     |  1.51 |    2 |
    | Shell |        3.5 | 20 to 80   | 3.5 mm  | 120 mm²/s (cSt)           |  2.17 |  1.5 |
    | Shell |          4 | 20 to 80   | 3.8 mm  | 120 mm²/s (cSt)           |  3.45 |    1 |
    | Shell |          5 | 20 to 80   | 4.6 mm  | 120 or 480 mm²/s (cSt)    |   6.5 |    1 |
    | Shell |          6 | 20 to 80   | 5.8 mm  | 480 mm²/s (cSt)           |  16.2 |  0.5 |"""
    if cup == 1:
        K = 0.226
        c = 13
    elif cup == 2:
        K = 0.567
        c = 5
    elif cup == 2.5:
        K = 0.925
        c = 3
    elif cup == 3:
        K = 1.51
        c = 2
    elif cup == 3.5:
        K = 2.17
        c = 1.5
    elif cup == 4:
        K = 3.45
        c = 1
    elif cup == 5:
        K = 6.5
        c = 1
    elif cup == 6:
        K = 16.2
        c = 0.5
    else:
        K = 0.226
        c = 13

    return K * (t - c)

def Ford_Cup(cup,t):
    """Convert the cup drain time (t) into kinematic viscosity values in mm²/s (cSt) for Ford Cups
    Following the data from ASTM D1200
    State Cup number followed by the time for example:
    Ford Cup #4 with a drain time of 80 seconds
    Ford_Cup(4,80)
    This should give you a reading of 290.7135 mm²/s (cSt)
    
    Equation is V = K(t−c)
    
    | Type  | Cup Number | Drain Time | Orifice | Recommended Oil Viscosity |   K   |  c   |
    |-------|------------|------------|---------|---------------------------|-------|------|
    | Ford  |          1 | 55 to 100  | 1.9 mm  | 20 mm²/s (cSt)            |  0.49 |   35 |
    | Ford  |          2 | 40 to 100  | 2.53 mm | 35 mm²/s (cSt)            |  1.44 |   18 |
    | Ford  |          3 | 20 to 100  | 3.4 mm  | 120 mm²/s (cSt)           |  2.31 | 6.58 |
    | Ford  |          4 | 20 to 100  | 4.12 mm | 120 mm²/s (cSt)           |  3.85 | 4.49 |
    | Ford  |          5 | 20 to 100  | 5.2 mm  | 460 mm²/s (cSt)           |  12.1 |  2.0 |"""
    if cup == 1:
        K = 0.49
        c = 35
    elif cup == 2:
        K = 1.44
        c = 18
    elif cup == 3:
        K = 2.31
        c = 6.58
    elif cup == 4:
        K = 3.85
        c = 4.49
    elif cup == 5:
        K = 12.1
        c = 2
    else:
        K = 0.49
        c = 35

    return K * (t - c)

def DIN_Cup_4mm(t):
    """Convert the cup drain time (t) into kinematic viscosity values in mm²/s (cSt) for Ford Cups
    Following the data from DIN 53211
    State Cup number followed by the time for example:
    DIN 4mm with a drain time of 80 seconds
    DIN_Cup_4mm(97)
    This should give you a reading of 438.6302 mm²/s (cSt)
    
    Equation is V = 4.57t-452/t
    | Type  | Cup Number | Drain Time | Orifice | Recommended Oil Viscosity |   A   |  B   |
    |-------|------------|------------|---------|---------------------------|-------|------|
    | DIN   | 4          | 25 to 150  | 4 mm    |                           |  4.57 |  452 |"""
    return 4.57 * t - 452 / t

def ISO_Cup(cup,t):
    """Convert the cup drain time (t) into kinematic viscosity values in mm²/s (cSt) for Ford Cups
    Following the data from ISO 2341
    State Cup number followed by the time for example:
    ISO Cup 3mm with a drain time of 57 seconds
    ISO_Cup(3,57)
    This should give you a reading of 21.7422 mm²/s (cSt)
    
    Equation is V = At-(B/t)
    | Type  | Cup Number | Drain Time | Orifice | Recommended Oil Viscosity |   A   |  B   |
    |-------|------------|------------|---------|---------------------------|-------|------|
    | ISO   | 3          | 30 to 100  | 3 mm    |                           | 0.443 |  200 |
    | ISO   | 4          | 30 to 100  | 4 mm    |                           |  1.37 |  200 |
    | ISO   | 5          | 30 to 100  | 5 mm    |                           |  3.28 |  220 |
    | ISO   | 6          | 30 to 100  | 6 mm    |                           |  6.90 |  570 |
    """
    if cup == 3:
        A = 0.443
        B = 200
    elif cup == 4:
        A = 1.37
        B = 200
    elif cup == 5:
        A = 3.28
        B = 220
    elif cup == 6:
        A = 6.90
        B = 570
    
    return A * t - (B / t)

def Ref_Oil(designation,oil_temp,V_TempL,TempL,V_TempH,TempH):
    """Corrects the mm²/s (cSt) for the Reference Oil used for calibration at a given temperature based upon information supplied on the calibration certificate.
    State the Reference Oil used followed by the measured temperature, then Viscosity at Lower Temperature, Lower Temperature followed
    by Viscosity at Higher Temperature, Higher Temperature. If you are unsure then the defaults will be used.
    Currently supported Oils are C10 and C100.
    For example: C10 oil measured at 21.3 °C, Viscosity at Lower Temperature 20.72 mm²/s (cSt), Lower Temperature of 20 °C,
    Viscosity at Higher Temperatures 16.92 mm²/s (cSt), Higher Temperatures 25 °C
    Ref_Oil('C10',23,20.72,20,16.92,25)
    This should give you a reading of 18.44 mm²/s (cSt)    
    """
    if designation in ['C10','c10','C 10','c 10']:
        if V_TempL <= 0 or TempL <= 0 or V_TempH <= 0 or TempH <= 0:
            V_TempL = 20.72
            TempL = 20
            V_TempH = 16.92
            TempH = 25
    elif designation in ['C100','c100','C 100','c 100']:
        if V_TempL <= 0 or TempL <= 0 or V_TempH <= 0 or TempH <= 0:
            V_TempL = 329.0
            TempL = 20
            V_TempH = 237.4
            TempH = 25
    return np.interp(oil_temp,[TempL,TempH],[V_TempL,V_TempH])

def Percentage_Error(Ref_Vis,Cup_Vis):
    """The maths required to calculate the percentage error between the Reference Viscosity and Measured Visocsity of the Cup. 
    The difference between the certified viscosity and the determined viscosity, multiplied by 100 and divided by the certified viscosity, will give the
    percentage variation of the cup from the standard.
    """
    return ((Ref_Vis - Cup_Vis) * 100) / Ref_Vis