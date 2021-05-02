# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

print ("Please input string")
a = input()
num_a = a.split(" ")
j=0
i=0
while i<= len(num_a)-1:
    if len(num_a[i])>5:
        j+=1
    i+=1
print("the number of words containing more than five letters: ", j)
