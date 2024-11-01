# Тесты

## Блочные тесты
Функция: solve(a: int, b: int, c: int) - Находит корни квадратного уравнения

Аргументы: a - коэффициент квадратного уравнения при x^2, b - коэффициент квадратного уравнения при x, c - свободный коэффициент.

Позитивные тесты:
 1. Тест ```test_two_roots``` (Тест с двумя корнями)
  - Входные данные: a = 1, b = -5, c = 4
  - Ожидаемый результат: [4, 1]
  
 2. Тест ```test_one_root``` (Тест с одним корнем (дискриминант равен 0))
  - Входные данные: a = 1, b = -6, c = 9
  - Ожидаемый результат: [ 3 ]

 3. Тест ```test_negative_discriminant``` (Тест с отрицательным дискриминантом)
  - Входные данные: a = 1, b = 1, c = 1
  - Ожидаемый результат: None

 4. Тест ```test_float_parametrs``` (Тест с вещественными числами)
  - Входные данные: a = 1.5, b = 6.8, c = 3
  - Ожидаемый результат: [-0.495289, -4.038044]

 5. Тест ```test_b_zero``` (Тест, когда коэффициент B равен 0)
  - Входные данные: a = 1, b = 0, c = -1
  - Ожидаемый результат: [1, -1]

 6. Тест ```test_c_zero``` (Тест, когда коэффициент C равен 0)
  - Входные данные: a = 1, b = -2, c = 0
  - Ожидаемый результат: [2, 0]
    
Негативные тесты:
 1. Тест ```test_a_zero``` (Тест, когда коэффициент A равен 0)
  - Входные данные: a = 0, b = 2, c = 1
  - Ожидаемый результат: ValueError

 2. Тест ```test_parametrs_not_number``` (Тест, когда коэффициент не числа)
  - Входные данные: a = "test", b = None, c = 1
  - Ожидаемый результат: TypeError
  
Функция: discriminant(a: int, b: int, c: int) - Находит дискриминант квадратного уравнения

Аргументы: a - коэффициент квадратного уравнения при x^2, b - коэффициент квадратного уравнения при x, c - свободный коэффициент

  1. Тест ```test_solve_discriminant``` (Проверка дискриминанта)
  - Входные данные: a = 2, b = 5, c = 2
  - Ожидаемый результат: 9
  
