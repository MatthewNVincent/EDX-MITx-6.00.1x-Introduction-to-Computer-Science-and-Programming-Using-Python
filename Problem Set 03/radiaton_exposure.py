def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    s = 0
    x = start
    while x < stop:
        s += f(x) * step
        x += step
    return s


print radiationExposure(40, 100, 1.5)
