# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    string = str(number)
    return string == string[::-1]


a = 10
b = 20
lst = list(map(palindrome, range(a, b + 1)))
# print(list(zip(range(a, b + 1), lst)))
num_palindrome = lst.count(True)
print(num_palindrome)
