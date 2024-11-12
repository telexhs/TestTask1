import TSP_calulate
import numpy as np  

def best_solution(tables):
    if not isinstance(tables, list):
        raise TypeError("На вход должен подаваться list")
    
    if len(tables ) == 0:
        raise ValueError("Список не должен быть пуст")
    
    min_table = TSP_calulate.Table([[]], None, 10000, [], [], [])
    for table in tables:
        if table.const <= min_table.const:
            min_table = table
    return min_table


def generate_path(solution):
    flag = True
    path = []
    start = 1
    path.append(start)
    while flag:
        for line in solution:
            if line[0] + 1 == start:
                if line[1] + 1 in path:
                    flag = False
                    break
                path.append(line[1] + 1)
                start = line[1] + 1
    return path


def kommi(matrix):
    if not isinstance(matrix, list):
        raise TypeError("На вход должен подаваться list")
    try:
        testMatrix = np.array(matrix)
    except:
        raise ValueError("Неправильный вид матрицы")
    if testMatrix.ndim != 2:
        raise ValueError("Неправильная размерность входной матрицы")
    
    testShape = testMatrix.shape
    if testShape[0] != testShape[1]:
        raise ValueError("Матрица должна быть квадратной")
    
    testDiag = np.diag(testMatrix)
    for element in testDiag:
        if element is not None:
            raise ValueError("Диагональные элементы должны быть None")

    table = TSP_calulate.Table(matrix, None, 0, [], [], [])
    solution = []
    solution.append(table)
    continue_flag = True
    sol = None

    while continue_flag:
        table = best_solution(solution)
        solution.remove(table)
        tableIn, tableOut, continue_flag = TSP_calulate.calculate_table(table)
        solution.append(tableIn)
        if tableOut is not None:
            solution.append(tableOut)
        if not continue_flag:
            sol = tableIn
    path = generate_path(sol.solution)
    return path, sol.const
