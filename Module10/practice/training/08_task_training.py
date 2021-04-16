# Прочитав число из файла задачи 7, определите:
# Какие цифры встречаются в числе чаще всего?
# Если несколько цифр встречаются одинаковое максимальное кол-во раз - найди любые.
# Является ли данное число(20000-значное) четным?
with open("huge_number.txt", "r") as f:
    s_number = f.readline().strip()

digits = {x: s_number.count(x) for x in s_number}
print(digits)

max_count = sorted(digits.values(), key=lambda x: -x)[0]
print("чаще всего встречаются цифры: ", list(filter(lambda kv: kv[1] == max_count, digits.items())))

print("четное: ", "да" if s_number[-1] in (0,2,4,6,8) else "нет")
