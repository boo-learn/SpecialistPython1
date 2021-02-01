# Подсчитать количество букв «а» во введенной строке

# TODO: your code here

text = 'English is a West Germanic language'

i = 0
j = 0
print(len(text))

while i < len(text):
    if text[i] == 'a':
        j += 1
    i += 1

print ('There is ', j, 'letters a in this text')
