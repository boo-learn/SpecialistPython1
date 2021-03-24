f = open("my_file.txt", "r", encoding="utf-8")
sym_count = 0


for line in f:
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    sym_count += len(line)
    # if line == "\n":
    #     lick_count += 1
    # for char in line:
    #     if char != " " and char != "\n":
    #         sym_count += 1

    print(line.rstrip())
print()
print("Число символов в файле -", sym_count)
