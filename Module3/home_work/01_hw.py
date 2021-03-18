# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

string = ""

for i in names: 
    string = string + i + ","

string = string[0:len(string)-1]
print (string)

# print(*names, sep=',') #StackOverflow portal recommendation
