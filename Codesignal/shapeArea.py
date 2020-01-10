def shapeArea(n):
    if n == 1:
        return n
    else :
        x = 1
        for i in range(1,n):
            a = x + 4 * i
            x = a
        return x
