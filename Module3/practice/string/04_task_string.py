# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
words = text.split()
i = 0
count = 0;
while i < len(words):
    if len(words[i]) > 5:
        count += 1
        print(words[i])
    i += 1
print('Количество слов:', count)
