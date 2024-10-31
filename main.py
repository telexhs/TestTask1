
import equations


if __name__ == '__main__':
    print('Введите коэфиценты уравнения Ax^2 + Bx+ C = 0')
    a, b, c = map(int, input().split())
    answer = equations.solve(a, b, c)
    print(answer)
    