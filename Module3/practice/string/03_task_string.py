# Подсчитать количество букв «а» во введенной строке

string = str(input("Please enter string: "))
char = "a" 
count = 0
i = 0

while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1

print ("Count of", char, "is", count) 
