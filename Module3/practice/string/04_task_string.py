# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Without using lists

# TODO: here we should trim trailing spaces
word_begin = 0
word_end = 0
word_end = text.find(' ', word_begin)
counter =  0
while word_end < len(text):
    word_end = text.find(' ', word_begin)
    word_length = word_end - word_begin
    #test_word = text[word_begin:word_end]    #for debug
    word_begin = word_end + 1
    if word_length > 5:
        counter +=1
