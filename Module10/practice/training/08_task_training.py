# Прочитав число из файла задачи 7, определите:
# Какие цифры встречаются в числе чаще всего?
# Если несколько цифр встречаются одинаковое максимальное кол-во раз - найди любые.
# Является ли данное число(20000-значное) четным?

file = open("data/generate_.txt", "r", encoding="utf-8")

digits = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

line = file.readline()

for char in line:
    digits[int(char)] += 1

last_digit = int(line[-1])

file.close()

print(digits)

print("чётное" if last_digit % 2 == 0 else "нечётное")
