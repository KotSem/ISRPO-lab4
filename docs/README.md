# Geometric Lib

## Общее описание решения
Библиотека `geometric_lib` предназначена для базовых геометрических расчетов на Python.
Включает функции для вычисления площади и периметра следующих фигур:
- Круг (`circle.py`)
- Квадрат (`square.py`)
- Прямоугольник (`rectangle.py`)
- Треугольник (`triangle.py`)

## Описание функций

### 1. circle.py
- `area(r)` — площадь круга по формуле `S = pi * r**2`.
- `perimeter(r)` — длина окружности по формуле `P = 2 * pi * r`.

### 2. square.py
- `area(a)` — площадь квадрата по формуле `S = a**2`.
- `perimeter(a)` — периметр квадрата по формуле `P = 4 * a`.

### 3. rectangle.py
- `area(a, b)` — площадь прямоугольника по формуле `S = a * b`.
- `perimeter(a, b)` — периметр прямоугольника по формуле `P = 2 * (a + b)`.

### 4. triangle.py
- `area(a, h)` — площадь треугольника по формуле `S = a * h / 2`.
- `perimeter(a, b, c)` — периметр треугольника по формуле `P = a + b + c`.

## Запуск Unit-тестов

Запуск всех тестов:
```bash
python -m unittest tests.py
```

Запуск тестов по отдельным фигурам:
```bash
python -m unittest test_circle.py
python -m unittest test_square.py
python -m unittest test_rectangle.py
python -m unittest test_triangle.py
```
