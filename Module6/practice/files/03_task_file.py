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

fruits = open('data/fruits.txt', 'r', encoding='utf-8')

fnames = dict()  # словарь с буквами (ключи) и дескрипторами файлов (значения)
for line in fruits:
    line = line.rstrip()
    if not line:
        continue

    liter = line[0]
    file_to_print = fnames.get(liter)

    if file_to_print:
        #file_to_print.write(line)
        print(line, file = file_to_print)
    else:
        file_to_print = open(liter + '.txt', 'w', encoding='utf-8')
        fnames[liter] = file_to_print
        #file_to_print.write(line)
        print(line, file=file_to_print)
for fil in fnames.values():
    fil.close()
