# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def gen_list(size, of, to):
    import random
    ret_list = []
    for _ in range(size):
        ret_list.append(random.randint(of, to))
    return ret_list


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
sz = int(input("Please enter size of list: "))

my_list = gen_list(sz, a, b)

print("List: ", my_list)

print("Palindromes count: ", count_palindrome(my_list))
