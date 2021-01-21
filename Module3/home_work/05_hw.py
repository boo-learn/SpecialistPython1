# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них
import random # Для вывода любого имени если их больше одного

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр", "Владислав", "Святослав"]

max_len = 0

for name in names:
    if len(name) > max_len:
        max_len = len(name)

#print('Максимальная длина:', max_len)

longest_names = []
for name in names:
    if len(name) == max_len:
        longest_names.append(name)

#print('Все самые длинные имена:', longest_names)

result_name = ''
# Выбор произвольного имени если их больше одного
if len(longest_names) > 1:
    n = random.randint(0, len(longest_names)-1)
    result_name = longest_names[n]
else:
    result_name = longest_names[0]
print(result_name)
