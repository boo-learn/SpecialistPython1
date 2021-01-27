# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 10
b = 70
print(list(map(lambda number: str(number) == str(number)[::-1], range(a, b+1))))
print(sum(map(lambda number: str(number) == str(number)[::-1], range(a, b+1))))
