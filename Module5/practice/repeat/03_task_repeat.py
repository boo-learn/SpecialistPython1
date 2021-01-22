# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    copy_num = number
    reverse_num = 0
    while number > 0:
        reverse_num += number % 10
        number //= 10
        if number > 0:
            reverse_num *= 10
    return reverse_num == copy_num

a = 11
b = 33
pali_list = []

for i in range(a, (b+1)):
    if palindrome(i) is True:
        pali_list.append(i)

print(pali_list)
