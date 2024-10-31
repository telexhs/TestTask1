import math

def solve(A:int, B:int, C:int):
    if A == 0:
        raise ValueError("Коэфицент A не должен быть нулем")
    D = discriminant(A, B, C) # Это дискриминант
    if D < 0:
        return None
    elif D == 0:
        x = -B / (2 * A)
        return [x]
    x1 =  (-B + math.sqrt(D)) / (2 * A)
    x2 =  (-B - math.sqrt(D)) / (2 * A)
    return [x1, x2]


def discriminant(A:int, B:int, C:int):
    return pow(B, 2) - 4 * A * C