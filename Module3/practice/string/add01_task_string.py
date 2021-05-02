# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку
text_check=text.replace(',','').replace('.','').replace('!','').replace('?','').replace('-','')
words = text_check.split(' ')
counter=i=0
while i<len(words):
    if len(words[i])>7:
        counter+=1
    i+=1
print(counter)
