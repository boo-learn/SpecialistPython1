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
letters = {}
f_fruits = open("data/fruits.txt", 'r', encoding="utf-8")
for line in f_fruits:
    stripped_line = line.strip()
    if stripped_line != "":
        letter = stripped_line[0]
        if letter in letters:
            letters[letter] += stripped_line + ","
        else:
            letters[letter] = stripped_line + ","
f_fruits.close()

for letter, fruit_list in letters.items():
    print(f"data/_fruits_{letter}.txt")
    f_fruit_grp = open(f"data/fruits_{letter}.txt", "w", encoding="utf-8")
    for fruit in fruit_list[:-1].split(","):
        f_fruit_grp.write(fruit + "\n")
    f_fruit_grp.close()
