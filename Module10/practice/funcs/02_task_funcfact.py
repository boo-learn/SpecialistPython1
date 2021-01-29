# Напишите функцию нахождения факториала числа n
# Примеры нахождения факториала:
# 5! = 1*2*3*4*5
# 7! = 1*2*3*4*5*6*7

def factorial(n):
    
    if n == 0:
        return 0
     
    if n > 1:
        return n * factorial(n -1)
    else:
        return 1

print(factorial(4))
