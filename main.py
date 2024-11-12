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
path, const = TSP.kommi(table)

print(f"Путь - {path}")
print(f"Константа - {const}")