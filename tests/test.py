from equations import solve, discriminant
import unittest
import math
import TSP, TSP_calulate
        
class TestFindRoots(unittest.TestCase):

    def test_two_roots(self):
        """Тест с двумя корнями"""
        a, b, c = 1, -5, 4
        answer = solve(a, b, c)
        self.assertIsNotNone(answer)
        self.assertEqual(len(answer), 2)
        self.assertEqual(answer[0], 4)
        self.assertEqual(answer[1], 1)

    def test_one_root(self):
        """Тест с одним корнем (дискриминант равен 0)"""
        a, b, c = 1, -6, 9
        answer = solve(a, b, c)
        self.assertIsNotNone(answer)
        self.assertEqual(len(answer), 1)
        self.assertEqual(answer[0], 3)

    def test_negative_discriminant(self):
        """Тест с отрицательным дискриминантом"""
        a, b, c = 1, 1, 1
        answer = solve(a, b, c)
        self.assertIsNone(answer)

    def test_float_parametrs(self):
        """Тест с вещественными числами"""
        a, b, c = 1.5, 6.8, 3
        answer = solve(a, b, c)
        self.assertAlmostEqual(answer[0], -0.495289, delta=0.0001)
        self.assertAlmostEqual(answer[1], -4.038044, delta=0.0001)

    def test_a_zero(self):
        """Тест, когда коэффициент A равен 0"""
        a, b, c = 0, 2, 1
        with self.assertRaises(ValueError):
            solve(a, b, c)

    def test_b_zero(self):
        """Тест, когда коэффициент B равен 0"""
        a, b, c = 1, 0, -1
        answer = solve(a, b, c)
        self.assertEqual(answer[0], 1)
        self.assertEqual(answer[1], -1)

    def test_c_zero(self):
        """Тест, когда коэффициент C равен 0"""
        a, b, c = 1, -2, 0
        answer = solve(a, b, c)
        self.assertEqual(answer[0], 2)
        self.assertEqual(answer[1], 0)

    def test_parametrs_not_number(self):
        """Тест с параметрами не числами"""
        a, b, c = "test", None, 1
        with self.assertRaises(TypeError):
            solve(a, b, c)

    def test_solve_discriminant(self):
        """Тест с проверкой дискриминанта"""
        a, b, c = 2, 5, 2
        answer = discriminant(a, b, c)
        self.assertEqual(answer, 9)
        a, b, c = 1, 1, 2
        answer = discriminant(a, b, c)
        self.assertEqual(answer, -7)

class Test_TSP_positive(unittest.TestCase):
    def test_solve_TSP(self):
        """Тест на общее решение задачи (размерность матрицы 6)"""
        table = [[None, 5, 6, 8, 5, 8],
                  [5, None, 4, 6, 6, 3],
                  [4, 3, None, 1, 9, 2],
                  [3, 4, 7, None, 5, 4],
                  [5, 4, 8, 8, None, 2],
                  [1, 6, 0, 3, 7, None]]
        path, const = TSP.kommi(table)
        self.assertEqual(const, 16)
        self.assertEqual(path, [1, 5, 2, 6, 3, 4])

    def test_solve_TSP(self):
        """Тест на общее решение задачи (размерность матрицы 4)"""
        table =    [[None, 10, 15, 20],
                    [10, None, 35, 25],
                    [15, 35, None, 30],
                    [20, 25, 30, None]]
        path, const = TSP.kommi(table)
        self.assertEqual(const, 80)
        self.assertEqual(path, [1, 3, 4, 2])


class Test_TSP_negative(unittest.TestCase):
    def test_TSP_wrong_input(self):
        """Неравильный аргумент на входе"""
        table1 = "matrix"
        
        with self.assertRaises(TypeError):
            path, const = TSP.kommi(table1)

    def test_TSP_wrong_matrix(self):
        """Неравильная матрица на входе"""
        table1 = [[None, [1, 2], 6, 8, 5, 8],
                  [5, None, 4, 6, 6, 3],
                  [4, 3, None, 1, 9, 2],
                  [3, 4, 7, None, 5, 4],
                  [5, 4, 8, 8, None, 2],
                  [1, 6, 0, 3, 7, None]]
        
        with self.assertRaises(ValueError):
            path, const = TSP.kommi(table1)

    def test_TSP_wrong_shape(self):
        """Неравильный размер матрицы"""
        table1 = [[None, 5, 6, 8, 5, 8],
                  [5, None, 4, 6, 6, 3],
                  [4, 3, None, 1, 9, 2],
                  [3, 4, 7, None, 5, 4],
                  [5, 4, 8, 8, None, 2]]
        
        with self.assertRaises(ValueError):
            path, const = TSP.kommi(table1)

    def test_TSP_wrong_diag(self):
        """Неравильные диагональные элементы"""
        table1 = [[8, 5, 6, 8, 5, 8],
                  [5, 1, 4, 6, 6, 3],
                  [4, 3, 2, 1, 9, 2],
                  [3, 4, 7, 3, 5, 4],
                  [5, 4, 8, 8, 9, 2],
                  [1, 6, 0, 3, 7, 0]]
        
        with self.assertRaises(ValueError):
            path, const = TSP.kommi(table1)

class Test_TSP_calculate_positive(unittest.TestCase):
    def test_avaliable_table_empty(self):
        """Тест проверки функции доступности ячейки таблицы"""
        table = TSP_calulate.Table(matrix=[[None, 1],[2, None]],iIgnored=[], jIgnored=[])
        result = TSP_calulate.is_avaliable(table=table, i=0, j=1)
        self.assertTrue(result)

    def test_avaliable_table_i(self):
        """Тест проверки функции доступности ячейки таблицы c заблокированной i-той строкой"""
        table = TSP_calulate.Table(iIgnored=[1], jIgnored=[])
        result = TSP_calulate.is_avaliable(table=table, i=1, j=1)
        self.assertFalse(result)

    def test_avaliable_table_diag(self):
        """Тест проверки функции доступности ячейки таблицы на диагонали"""
        table = TSP_calulate.Table(matrix=[[None, 1],[2, None]], iIgnored=[], jIgnored=[])
        result = TSP_calulate.is_avaliable(table=table, i=1, j=1)
        self.assertFalse(result)

    def test_calculate_const1(self):
        """Тест рассчета константы"""
        matrix =   [[None, 10, 15, 20],
                    [10, None, 35, 25],
                    [15, 35, None, 30],
                    [20, 25, 30, None]]
        table = TSP_calulate.Table(matrix=matrix)
        TSP_calulate.calculate_const(table)
        self.assertEqual(table.const, 70)

    def test_calculate_const2(self):
        """Тест рассчета константы"""
        matrix =   [[None, 1],
                    [2, None]]
        table = TSP_calulate.Table(matrix=matrix)
        TSP_calulate.calculate_const(table)
        self.assertEqual(table.const, 3)

    def test_fix_Hamilton_circuit1(self):
        """Тест с проверкой функции исправление гамильтонова цикла без других решений"""
        matrix1 = [[None, 10, 15, 20],
                    [10, None, 35, 25],
                    [15, 35, None, 30],
                    [20, 25, 30, None]]
        
        matrix2 = [[None, 10, 15, 20],
                    [10, None, 35, 25],
                    [None, 35, None, 30],
                    [20, 25, 30, None]]
        table = TSP_calulate.Table(matrix=matrix1, solution=[(0, 2)])
        TSP_calulate.fix_Hamilton_circuit(table, (0, 2))
        self.assertEqual(table.matrix, matrix2)

    def test_fix_Hamilton_circuit2(self):
        """Тест с проверкой функции исправление гамильтонова цикла с другими решениями"""
        matrix1 = [[None, 10, None, 20],
                    [10, None, 35, 25],
                    [None, 35, None, 30],
                    [20, 25, 30, None]]
        
        matrix2 = [[None, 10, None, 20],
                    [None, None, 35, 25],
                    [None, 35, None, 30],
                    [20, 25, 30, None]]
        table = TSP_calulate.Table(matrix=matrix1, solution=[(0, 2), (3, 1), (2, 3)])
        TSP_calulate.fix_Hamilton_circuit(table, (2, 3))
        self.assertEqual(table.matrix, matrix2)

    def test_fix_Hamilton_circuit2(self):
        """Тест с расчетом таблицы"""
        matrix1 = [[None, 10, 15, 20],  
                    [10, None, 35, 25],
                    [15, 35, None, 30],
                    [20, 25, 30, None]] 

        matrix2 = [[None, 0, 0, None],
                    [0, None, 15, 0],
                    [0, 15, None, 0],
                    [0, 5, 5, None]]
        
        matrix3 = [[None, 0, 0, 0],
                    [0, None, 20, 5],
                    [0, 20, None, 5],
                    [None, 0, 0, None]]
        table = TSP_calulate.Table(matrix=matrix1)
        tablein, tableout, check = TSP_calulate.calculate_table(table)

        self.assertEqual(tablein.matrix, matrix2)
        self.assertEqual(tableout.matrix, matrix3)

        self.assertEqual(tablein.const, 80)
        self.assertEqual(tableout.const, 75)

        self.assertEqual(tablein.solution, [(3, 0)])
        self.assertEqual(tableout.solution, [])

        self.assertEqual(tablein.iIgnored, [3])
        self.assertEqual(tablein.jIgnored, [0])

        self.assertEqual(tableout.iIgnored, [])
        self.assertEqual(tableout.jIgnored, [])
if __name__ == '__main__':
    unittest.main()