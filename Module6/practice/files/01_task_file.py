# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

f_limericks = open("data/limericks.txt", "r", encoding="utf-8")

count_letters = 0
count_limericks = 1

for line in f_limericks:
    if len(line) == 1:
        count_limericks += 1
    print(line.rstrip())
    for letter in line:
        if letter.isalnum():
            count_letters += 1

print(f"\nКоличество стихов: {count_limericks}\n")
print(f"Количество букв: {count_letters}")
