#!/usr/bin/python3
def magic_calculation(a, b):
    rVal = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                rVal += a ** b / i
        except:
            rVal = b + a
            break
    return rVal
