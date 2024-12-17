from math import *   # Подключение модуля math
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))

a1 = abs(cos(x)-cos(y)**2*sin(y)**2)
a2 = (1+z+(z**2/2))
s= a1*a2
print("Результат ",s)
