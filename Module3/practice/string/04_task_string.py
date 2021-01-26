# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
new_text = []
new_text = text.split(' ')
count = 0
y = 0
for i in new_text:
    lenght = len(new_text[y])
    y = y + 1
    if lenght > 5:
        count += 1
print(count)
