# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here

# 1-й вариант с передобром символов строки - не обрабатывается последнее слово
i = 0
len_word = 0
num_long_word = 0
while i < len(text):
    if text[i] == " " or i == len(text)-1:
        if len_word > 5:
            num_long_word += 1
        len_word = 0
    else:
        len_word += 1
    i += 1
print(num_long_word)

# 2-ой вариант с методами строки и списка

text1 = text.split()
i = 0
c = 0
while i < len(text1):
    if len((text1[i])) > 5:
        c += 1
    i += 1

print(c)
