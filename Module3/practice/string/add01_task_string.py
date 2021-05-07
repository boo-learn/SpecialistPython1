# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

symbols_to_replace = ",.!?-"

for c in symbols_to_replace:
    text = text.replace(c, "")
cnt = 0  # счетчик слов
word = ""
for c in range(len(text)):
    if text[c] != " ":
        word = word + text[c]
        continue
    if len(word) > 7:
        cnt += 1
    word = ""
print(cnt)
