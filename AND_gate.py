def AND(x, y):
    if x == 0 and y == 0:
        return 0
    if x == 0 and y == 1:
        return 0
    if x == 1 and y == 0:
        return 0
    else:
        return 1
