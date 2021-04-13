# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

text = input('Строка: ')
count = 0
mas_text = text.split(' ')
for i in range(len(mas_text)):
    if len(mas_text[i]) > 5:
        count += 1
print(f'Количество слов длиной больше 5 символов: {count}')
