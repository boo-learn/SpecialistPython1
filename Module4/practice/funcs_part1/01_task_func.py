# Напишите функцию, возвращающую наибольшее из двух чисел

def max2(n1, n2):
    if n1>n2:
        result = n1
    else:
        result = n2
    return result

# Тестируем функцию
print(max2(6, 6))
print(max2(-10, -12))
print(max2(2.5, 2.6))
print(max2(-2.5, 0))
print(max2(0, -2.5))


# Тестируем функцию
print(max2(5, 6))
print(max2(-10, -12))
print(max2(2.5, 2.6))
print(max2(-2.5, 0))
print(max2(0, -2.5))
