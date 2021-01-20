# Подсчитать количество букв «а» во введенной строке

# TODO: your code here
word = input('Введите слово')
x = 0
y = 0
while x < len(word):
    if word[x] == 'а':
        y += 1
    x += 1
print(y)
