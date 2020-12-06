# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
text = text.split()
i = len(text)
c = 0;
n=0;
while n<i-1:
    if(len(text[n])>5):
        c += 1
    n=n+1
print(c)
