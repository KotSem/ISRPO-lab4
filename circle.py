import math


def area(r):
    '''
    Принимает радиус r (int / float).
    Возвращает площадь круга (float): S = pi * r**2.
    Пример вызова: area(5) -> 78.5398
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус r (int / float).
    Возвращает длину окружности (float): P = 2 * pi * r.
    Пример вызова: perimeter(5) -> 31.4159
    '''
    return 2 * math.pi * r
