# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

splitted = text.split(' ')

i = 0
counter = 0
print(len(splitted))

while i < len(splitted):
    if len(splitted[i]) > 5:
        counter += 1
    i += 1

print(counter)
