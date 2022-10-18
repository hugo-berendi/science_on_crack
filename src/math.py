def heron(n: float, error: float):
    y = (n + n / n) / 2
    while abs(y - n / y) > error:
        y = (y + n / y) / 2
    return y