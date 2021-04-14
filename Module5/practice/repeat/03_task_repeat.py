# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
a = 10
b = 99


def palindrome(number):
    return str(number) == str(number)[::-1]


def count_palindrome(of, to):
    total = 0
    for i in range(of, to + 1):
        total += palindrome(i)
    return total
  
  
  print(count_palindrome(a, b))
  
