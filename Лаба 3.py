import math

# Исходные данные
a = 4
b = 7
x1 = 2
xn = 5
dx = 0.1

# Вычисление с использованием for
x = x1
print("Результаты вычислений (for):")
for x in [x1 + i * dx for i in range(int((xn - x1) / dx) + 1)]:
    y = b * x * math.sqrt(1 + a**2 * math.log(x))
    print(f"x = {x:.1f}, y = {y:.4f}")

print("Результаты вычислений (while):")
while x <= xn:
    y = b * x * math.sqrt(1 + a**2 * math.log(x))
    print(f"x = {x:.1f}, y = {y:.4f}")
    x += dx