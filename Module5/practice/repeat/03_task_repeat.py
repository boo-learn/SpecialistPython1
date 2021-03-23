# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    temp = number
    number_rev = 0
    while temp > 0:
        number_rev = number_rev * 10 + temp % 10  # take last digit in the original number, place it at the beginning of new one
        temp = temp // 10  # shift the original number to the right
    return number == number_rev


def count_palindrome(list_param):
    count_p = 0
    for el in list_param:
        if palindrome(el):
            count_p += 1
    return count_p


a = int(input("Please enter A: "))
b = int(input("Please enter B: "))

num_palindromes = count_palindrome(list(range(a, b+1)))

print("Palindromes count: ", num_palindromes)
