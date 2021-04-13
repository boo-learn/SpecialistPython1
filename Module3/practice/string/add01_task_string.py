# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку
text = input('Строка: ')
count = 0
text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('?', '-')
mas_text = text.split(' ')

for i in range(len(mas_text)):
    if len(mas_text[i]) > 7:
        count += 1

print(f'Количество слов длиной больше 7 символов: {count}')
