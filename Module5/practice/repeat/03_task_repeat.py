# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    revers=0
    num=number
    while number:
        revers=revers*10+number%10
        number//=10
    return revers==num

a = 111
b = 191
count=0
for i in range(abs(a-b)+1):
    if palindrome(a+i):
       count+=1

print(f"Чисел палиндромов получилось: {count}")
