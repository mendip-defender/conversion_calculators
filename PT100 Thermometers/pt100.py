""" The following maths are various formulas related to the use of PT100 thermometers based on the information in
BS EN 60751: 2008 - Industrial platinum resistance thermometers and platinum temperature sensors.

Use this at your peril, check the maths.

Copyright © 2024-07-06 https://github.com/mendip-defender/"""

def calculate_class(ref_t, uuc_t):
    """Using the Reference Temperature (ref_t) and the Unit Under Calibration Temperature (uuc_t),
     * Calculate the difference as an absolute
     * Calculate the various tolerances classes based on BS EN 60751: 2008
     * Determined which class that reading would be placed in.
    It will return,
     - ref_t = Reference Temperature
     - uuc_t = Under Calibration Temperature
     - diff_r = Difference between the two readings rounded to 4 digits after the decimal
     - grade = The class the reading falls into, Unknown will display if it is outside the tolerance.
     - aa_spec = The calculated tolerance for AA Class
     - a_spec = The calculated tolerance for A Class
     - b_spec = The calculated tolerance for B Class
     - c_spec = The calculated tolerance for C Class
    
    """
    n = 4
    diff = ref_t - uuc_t
    diff_abs = abs(diff)
    diff_r = round(diff, n)
    aa_spec = round((0.1 + (0.0017 * ref_t)), n)
    a_spec = round((0.15 + (0.0017 * ref_t)), n)
    b_spec = round((0.3 + (0.0017 * ref_t)), n)
    c_spec = round((0.6 + (0.0017 * ref_t)), n)
    if diff_abs < aa_spec:
        grade = 'Class AA'
    elif diff_abs >= aa_spec and diff < a_spec:
        grade = 'Class A'
    elif diff_abs >= a_spec and diff < b_spec:
        grade = 'Class B'
    elif diff_abs >= b_spec and diff < c_spec:
        grade = 'Class C'
    else:
        grade = 'Unknown'
    return (diff_r, grade, aa_spec, a_spec, b_spec, c_spec, ref_t, uuc_t)

def temp_to_ohm(temp):
    """Using a given Temperature (temp), this function will calculate the resistance based on the coefficients in BS EN 60751: 2008
    It will return,
     - t = The inputted Temperature (temp)
     - Rt = Resistance value.
    
    """
    t = temp
    R0 = 100 
    if t > -201 and t < 0:
        A = 3.9083 * 10**-3
        B = -5.775 * 10**-7
        C = -4.183 * 10**-12
        Rt = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
    elif t >= 0 and t < 851:
        A = 3.9083 * 10**-3
        B = -5.775 * 10**-7
        C = 0 * 10**-12
        Rt = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
    else:
        print('error')
    return (t, Rt)

def ohm_to_temp(ohm,n):
    """Using a given Resistance (ohm) and Number of digits (n) to output the Temperature (t) this function will calculate
    the temperature based on the coefficients in BS EN 60751: 2008, using a while loop to keep reiterating through the numbers until it finds the same number.
    Due to the slowness of this method, I have split the loops so that they search over a smaller zone.
    It will return,
     - Rt = The inputted resistance
     - t = Temperature

    """
    Rt = ohm
    R0 = 100
    digits = 10**-n
    if Rt > 18 and Rt < 100:
        A = 3.9083 * 10**-3
        B = -5.775 * 10**-7
        C = -4.183 * 10**-12
        if Rt > 18 and Rt < 39.7232: # -200 °C to -150 °C
            t = -201
            Rt0 = 18
            while Rt0 < Rt:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt0 == Rt:
                    break
                t += digits
        elif Rt > 39.7232 and Rt < 60.2558: # -150 °C to -100 °C 
            t = -151
            Rt0 = 39
            while Rt0 < Rt:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt0 == Rt:
                    break
                t += digits
        elif Rt > 60.2558 and Rt < 80.3063: # -100 °C to -50 °C 
            t = -101
            Rt0 = 59
            while Rt0 < Rt:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt0 == Rt:
                    break
                t += digits
        else: # -50 °C to 0 °C 
            t = -51
            Rt0 = 79
            while Rt0 < Rt:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt0 == Rt:
                    break
                t += digits
    elif Rt >= 100 and Rt < 400:
        A = 3.9083 * 10**-3
        B = -5.775 * 10**-7
        C = 0 * 10**-12
        if Rt > 100 and Rt < 138.5055: # 0 °C to 100 °C
            t = -1
            Rt0 = 99
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        elif Rt > 138.5055 and Rt < 175.8560: # 100 °C to 200 °C
            t = 99
            Rt0 = 138
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        elif Rt > 175.8560 and Rt < 212.0515: # 200 °C to 300 °C
            t = 199
            Rt0 = 175
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        elif Rt > 212.0515 and Rt < 247.092: # 300 °C to 400 °C
            t = 299
            Rt0 = 211
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        elif Rt > 247.092 and Rt < 280.9775: # 400 °C to 500 °C
            t = 399
            Rt0 = 246
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        elif Rt > 280.9775 and Rt < 313.708: # 500 °C to 600 °C
            t = 499
            Rt0 = 280
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        elif Rt > 313.708 and Rt < 345.2835: # 600 °C to 700 °C
            t = 599
            Rt0 = 313
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        elif Rt > 345.2835 and Rt < 375.704: # 700 °C to 800 °C
            t = 699
            Rt0 = 344
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
        else: # >800 °C
            t = 799
            Rt0 = 375
            while Rt > Rt0:
                Rt0 = R0*(1 + A*t + B*t**2 + C*(t - 100)*t**3)
                if Rt == Rt0:
                    break
                t += digits
    else:
        print('error')
    return (Rt, t)