import math

def solve(a:int, b:int, c:int):
    if a == 0:
        raise ValueError("Коэфицент A не должен быть нулем")
    D = discriminant(a, b, c) # Это дискриминант
    if D < 0:
        return None
    elif D == 0:
        x = -b / (2 * a)
        return [x]
    x1 =  (-b + math.sqrt(D)) / (2 * a)
    x2 =  (-b - math.sqrt(D)) / (2 * a)
    return [x1, x2]


def discriminant(a:int, b:int, c:int):
    return pow(b, 2) - 4 * a * c