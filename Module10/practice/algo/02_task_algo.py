# Игра “Компьютер угадывает число”
# Пользователь загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у него “Твое число равно, меньше или больше чем число N?”,
# где N - число, которое хочет проверить компьютер.
# Пользователь отвечает одним из трех чисел: 1 - равно, 2 - больше, 3 - меньше
# Напишите программу, которая с помощью цепочки таких вопросов и ответов пользователя угадывает число

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за 7 попыток.

min = 1
max = 100
answer = 0
while answer != 1:
    print('Твое число равно, меньше или больше чем число', (min+max)//2, '?')
    answer = int(input())
    if answer == 2:
        min=(min+max)//2+1
    elif answer == 3:
        max=(min+max)//2-1
print('Ваше число: ', (min+max)//2)
