import equations
import TSP


#print('Введите коэфиценты уравнения Ax^2 + Bx+ C = 0')
#a, b, c = map(int, input().split())
#answer = equations.solve(a, b, c)
#print(answer)
    
table =    [[None, 10, 15, 20],
            [10, None, 35, 25],
            [15, 35, None, 30],
            [20, 25, 30, None]]

table1 =   [[None, 5, 6, 8, 5, 8],
            [5, None, 4, 6, 6, 3],
            [4, 3, None, 1, 9, 2],
            [3, 4, 7, None, 5, 4],
            [5, 4, 8, 8, None, 2],
            [1, 6, 0, 3, 7, None]]

table2 =   [[None, 7, 16, 21, 2, 17],
            [13, None, 21, 15, 43, 23],
            [25, 3, None, 31, 17, 9],
            [13, 10, 27, None, 33, 12],
            [9, 2, 19, 14, None, 51],
            [42, 17, 5, 9, 23, None]]
path, const = TSP.kommi(table2)

print(f"Путь - {path}")
print(f"Константа - {const}")