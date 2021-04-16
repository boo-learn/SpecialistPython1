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
import os
from settings import BASE_DIR

file_path = os.path.join(BASE_DIR, "Files", "fruits.txt")
f = open(file_path, "r", encoding="utf-8")
lst_f = list(map(lambda x: x.replace("\n", ""), list(f)))
lst_f.sort()
lst_f = lst_f[lst_f.count(""):]
first_letters = set(map(lambda x: x[0], lst_f))
for el in first_letters:
    file_name = f"fruits-{el}.txt"
    file_path = os.path.join(BASE_DIR, "Files", file_name)
    f = open(file_path, "w", encoding="utf-8")
    slice_by_letter=list(filter(lambda x:x[0]==el,lst_f))
    for i in slice_by_letter:
        f.write(f"{i}\n")
    f.close()
