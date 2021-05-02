# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# 1-й вариант
longest_name_index = 0
name_lnt = 0
for name in names:
    if len(name) > name_lnt:
        name_lnt = len(name)
        longest_name_index = names.index(name)
print(names[longest_name_index])

# 2-й вариант
names.sort(key=len)
print(names[-1])
