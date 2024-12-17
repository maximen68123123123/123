#зад 1
# Ввод количества элементов списка
n = int(input("Введите количество элементов списка -> "))
x = []

# Ввод элементов списка
for i in range(n):
    x.append(int(input(f"Введите элемент {i} -> ")))

# Находим максимальный элемент и его индекс
max_element = max(x)
max_index = x.index(max_element)

print("Исходный список: ", x)
print("Максимальный элемент: ", max_element)
print("Порядковый номер максимального элемента: ", max_index)

#зад  2
## Ввод количества элементов списка
n = int(input("Введите количество элементов списка -> "))
x = []

# Ввод элементов списка
for i in range(n):
    x.append(int(input(f"Введите элемент {i} -> ")))

# Получаем список нечетных чисел
odd_numbers = [num for num in x if num % 2 != 0]

# Проверяем, есть ли такие числа и сортируем
if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Новый список нечетных чисел в порядке убывания: ", odd_numbers)
else:
    print("Нечетных чисел нет.")