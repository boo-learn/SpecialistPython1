# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
f = open('data/fruits.txt', 'r', encoding='utf-8')
fruits = []
alphabet = list(map(chr, range(ord('А'), ord('Я')+1)))

for line in f:
    if line.rstrip() != '':
        fruits.append(line.strip())

f.close()

for letter in alphabet:
    list_fruits = ''
    for fruit in fruits:
        if fruit[0] == letter:
            list_fruits += fruit + '\n'
    if list_fruits != '':
        f_write = open(f'data/fruits/fruits_{letter}.txt', 'w', encoding='utf-8')
        f_write.write(list_fruits)
        f_write.close()
