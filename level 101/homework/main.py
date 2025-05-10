# 1

def burner(c, h, o):
    water = min(h // 2, o)
    h -= water * 2
    o -= water

    co2 = min(c, o // 2)
    c -= co2
    o -= co2 * 2

    methane = min(c, h // 4)

    return (water, co2, methane)


# 2

import math

def stack_height_2d(layers):
    if layers == 0:
        return 0
    return 1 + (layers - 1) * (math.sqrt(3) / 2)


# 3

def height(n):
    if n == 0:
        return "{:.3f}".format(2000000)
    
    total_height = 2000000 * (1 - 2.5**n) / (1 - 2.5)
    
    return "{:.3f}".format(total_height)