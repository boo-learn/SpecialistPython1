# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
max=""
for elm in names:
    if(len(max)<len(elm)):
        max=elm
print(max)
