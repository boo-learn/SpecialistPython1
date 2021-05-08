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

f = open("fruits.txt", "r", encoding="utf-8")

d = {}
for word in f:
    if word.strip() == "":
        continue

    if d.get(word[0]) is None:
        d[word[0]] = []
    val = d[word[0]]
    val.append(word.rstrip())
    d[word[0]] = val
print(d)
f.close()

for key, val in d.items():
    f = open(f"data/fruits_{key}.txt", "w", encoding="utf-8")
    for fruit in val:
        f.write(fruit + "\n")
    f.close()
