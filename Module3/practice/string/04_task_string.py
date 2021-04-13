# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
t = text

ind = -1
while t != "":
    ind = t.find(" ")
    if ind >= 5:
        print(t[:ind])
        t = t[ind + 1:]
    elif ind == -1:
        if len(t) >= 5:
            print(t)
        t = ""
    else:
        t = t[ind + 1:]
