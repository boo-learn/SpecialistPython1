# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

x = 0
y = 0
z = 0
while x < len(text):
    if text[x] == ' ':
        y = 0
    elif y == 6:
        z += 1
    y += 1
    x += 1
print(z)
