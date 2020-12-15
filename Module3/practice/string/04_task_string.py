# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
list=text.split(" ")
i=0
count=0
while i<len(list):
    if len(list[i])>5:
        count+=1
    i+=1
print(text)
print("Количество слов больше 5 символов в тексте равно: ",count)
# TODO: your code here
