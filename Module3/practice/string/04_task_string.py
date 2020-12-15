# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
splt = text.split(' ')
num_words = len(splt)

print(splt)

i = 0
res = 0
while i<num_words:
    if len(splt[i]) > 5:
        res +=1
    i += 1
print(res, 'слов длиной более 5 букв')
