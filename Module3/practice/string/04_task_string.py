# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

string = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
words = string.split(" ")


i = 0
count = 0
for word in words:
    if len(word) > 5:
        count = count + 1

print(count)
