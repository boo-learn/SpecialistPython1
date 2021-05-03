# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    temp_number = number
    list_number = []
    while temp_number != 0:
        list_number.append(temp_number % 10)
        temp_number //= 10
    if list_number[::-1] == list_number:
        return True
    return False


a = 10
b = 20000

palindrome_range = []

for i in range(a, b):
    if palindrome(i):
        palindrome_range.append(i)

print(palindrome_range)
