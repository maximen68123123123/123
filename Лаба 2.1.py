from math import *
import sys

# Ввод значений
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))

# Выбор функции f(x)
msg = "Выберите вид функции f(x): arcsin(v/x) -> 1, e^x -> 2, ln(x*y) -> 3"
f = float(input(msg + "\n -> "))
fx = None

# Определение значения f(x)
match f:
    case 1:
        if abs(y/x) <= 1:  # Проверка области определения arcsin
            fx = asin(y/x)
        else:
            print("Значение arcsin не может быть вычислено")
            sys.exit()
    case 2:
        fx = exp(x)
    case 3:
        if x*y > 0:  # Проверка области определения ln
            fx = log(x*y)
        else:
            print("Значение ln не может быть вычислено")
            sys.exit()
    case _:
        print("Неверный выбор")
        sys.exit()

# Вычисление d в зависимости от условий
d = None
if x > y:
    # Проверка, что подкоренное выражение неотрицательно
    if fx - y + tan(fx) >= 0:
        d = pow(fx - y + tan(fx), 1/3)
    else:
        d = "значение не может быть вычислено"
elif x < y:
    d = pow(y - fx, 2) + cos(fx)
elif x == y:
    d = pow(y + fx, 2) + pow(x, 2)

print("Результат: ", d)
