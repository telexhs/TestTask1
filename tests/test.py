from equations import solve, discriminant
import unittest
import math


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
        


if __name__ == '__main__':
    unittest.main()