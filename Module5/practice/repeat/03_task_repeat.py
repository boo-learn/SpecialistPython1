# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    s_num = str(number)
    if s_num == s_num[::-1]:
        return True
    return False
a = 10
b = 222
my_lst = []
for n in range(a, b, 3):
    if palindrome(n):
        my_lst.append(n)
print(my_lst)
