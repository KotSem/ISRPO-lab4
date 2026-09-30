def area(a, h):
    '''
    Принимает сторону a и высоту h (int / float).
    Возвращает площадь треугольника (float): S = a * h / 2.
    Пример вызова: area(6, 4) -> 12.0
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Принимает стороны треугольника a, b, c (int / float).
    Возвращает периметр треугольника (int / float): P = a + b + c.
    Пример вызова: perimeter(3, 4, 5) -> 12
    '''
    return a + b + c
