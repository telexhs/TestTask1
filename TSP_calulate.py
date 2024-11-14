import copy


class Table:
    def __init__(self, matrix=None, const=0, iIgnored=[], jIgnored=[], solution=[]):
        self.matrix = matrix
        self.const = const
        self.iIgnored = iIgnored
        self.jIgnored = jIgnored
        self.solution = solution


def is_avaliable(table, i=None, j=None):
    if i is None and j is not None:
        return j not in table.jIgnored
    elif j is None:
        return i not in table.iIgnored
    else:
        if i in table.iIgnored:
            return False
        if j in table.jIgnored:
            return False
        if table.matrix[i][j] is None:
            return False
        return True


def calculate_const(table):
    Ui = []
    Vj = []
    length =  len(table.matrix)
    for i in range(0, length):
        minI = 1000
        if not is_avaliable(table, i):
            continue
        for j in range(0, length):
            if not is_avaliable(table, i, j):
                continue
            minI = min(minI, table.matrix[i][j])

        for j in range(0, length):
            if not is_avaliable(table, i, j):
                continue
            table.matrix[i][j] = table.matrix[i][j] - minI
        Ui.append(minI)

    for j in range(0, length):
        minJ = 1000
        if not is_avaliable(table, i=None, j=j):
            continue
        for i in range(0, length):
            if not is_avaliable(table, i, j):
                continue
            minJ = min(minJ, table.matrix[i][j])

        for i in range(0, length):
            if not is_avaliable(table, i, j):
                continue
            table.matrix[i][j] = table.matrix[i][j] - minJ
        Vj.append(minJ)
    const = 0
    for val in Ui:
        const = const + val
    for val in Vj:
        const = const + val
    table.const = table.const + const
    return table


def fix_Hamilton_circuit(table, last_solution):
    start = last_solution[0]
    end = last_solution[1]
    restart = True
    while restart:
        restart = False
        for sol in table.solution:
            if sol != last_solution:
                if sol[0] == end:
                    end = sol[1]
                    restart = True
                if sol[1] == start:
                    start = sol[0]
                    restart = True
    table.matrix[end][start] = None


def calculate_table(table):
    table = calculate_const(table)
    length =  len(table.matrix)
    continue_flag = True
    max_NPi = 100
    max_NPj = 100
    max_NullPower = -1
    for i in range(0, length):
        if not is_avaliable(table, i):
            continue
        for j in range(0, length):
            if not is_avaliable(table, i, j):
                continue
            if table.matrix[i][j] == 0:
                minJ = 100
                minI = 100
                fix = True
                for NPj in range(0, length):
                    if not is_avaliable(table, i, NPj) or NPj == j:
                        continue
                    try:
                        minJ = min(minJ, table.matrix[i][NPj])
                    except:
                        print(f"ij ={table.matrix[i][j]}, iNPj ={table.matrix[i][NPj]}; i- {i}, j- {j}; i- {i}, NPj- {NPj}")
                    fix = False

                for NPi in range(0, length):
                    if not is_avaliable(table, NPi, j) or NPi == i:
                        continue
                    minI = min(minI, table.matrix[NPi][j])
                    fix = False

                if not fix:
                    if max_NullPower <= minJ + minI:
                        max_NullPower = minI + minJ
                        max_NPi = i
                        max_NPj = j
    if fix:
        in_iIgnored_list = table.iIgnored.copy()  
        in_jIgnored_list = table.jIgnored.copy()
        in_solution_list = table.solution.copy()
        in_matrix = copy.deepcopy(table.matrix)
        for last_i in range(0, length):
            for last_j in range(0, length):
                if is_avaliable(table, last_i, last_j):

                    in_iIgnored_list.append(last_i)

                    in_jIgnored_list.append(last_j)

                    in_solution_list.append((last_i, last_j))

                    tableIn = Table(in_matrix, table.const, in_iIgnored_list, in_jIgnored_list, in_solution_list)

                    fix_Hamilton_circuit(tableIn, (last_i, last_j))
                    #tableIn = calculate_const(tableIn)

                    continue_flag = False
                    tableOut = None
    else:
        # Вариант с рассмотрением дуги
        in_iIgnored_list = table.iIgnored.copy()
        in_iIgnored_list.append(max_NPi)

        in_jIgnored_list = table.jIgnored.copy()
        in_jIgnored_list.append(max_NPj)

        in_solution_list = table.solution.copy()
        in_solution_list.append((max_NPi, max_NPj))

        in_matrix = copy.deepcopy(table.matrix)

        tableIn = Table(in_matrix, table.const, in_iIgnored_list, in_jIgnored_list, in_solution_list)

        fix_Hamilton_circuit(tableIn, (max_NPi, max_NPj))
        #tableIn = calculate_const(tableIn)

    # Вариант с исключённой дугой
        out_iIgnored_list = table.iIgnored.copy()
        out_jIgnored_list = table.jIgnored.copy()
        out_solution_list = table.solution.copy()
        out_matrix = copy.deepcopy(table.matrix)

        tableOut = Table(out_matrix, table.const, out_iIgnored_list, out_jIgnored_list, out_solution_list)
        tableOut.matrix[max_NPi][max_NPj] = None
        #tableOut = calculate_const(tableOut)

    return tableIn, tableOut, continue_flag