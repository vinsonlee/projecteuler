# hash of computed routes
R = {}


def routes(x, y):
    h = hash((x, y))

    if h in R:
        return R[h]
    elif x == 0 and y == 0:
        return 0
    elif x == 0 and y > 0:
        return 1
    elif x > 0 and y == 0:
        return 1
    else:
        r = routes(x, y - 1) + routes(x - 1, y)
        R[h] = r
        return r


print routes(20, 20)
