import math

def solve(a, b, c):
    if type(a) != int and type(a) != float:
        raise TypeError("Параметр 'a' должен быть числом")
        
    if type(b) != int and type(b) != float:
        raise TypeError("Параметр 'b' должен быть числом")
    
    if type(c) != int and type(c) != float:
        raise TypeError("Параметр 'c' должен быть числом")
        
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


def discriminant(a, b, c):
    return pow(b, 2) - 4 * a * c