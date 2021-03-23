# Найдите количество чисел, являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 1
b = 55


def palindrome(number):
    number = str(number)
    if len(number) < 2:
        return

    palindrome = number[::-1]

    return palindrome == number


numbers = []
for el in range(a, b + 1):
    numbers.append(el)

matched = []
for number in numbers:
    if palindrome(number):
        matched.append(number)

print(matched)
