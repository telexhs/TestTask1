import math

def solve(A:int, B:int, C:int):
    D = discriminant(A, B, C)
    if D < 0:
        return None
    x1 =  (-B + math.sqrt(D)) / (2 * A)
    x2 =  (-B - math.sqrt(D)) / (2 * A)
    return [x1, x2]


def discriminant(A:int, B:int, C:int):
    return pow(B, 2) - 4 * A * C