# При решении различных задач данной практики вы написали некоторое количество функций. В
# озможно, в дальнейшем вы захотите использовать эти функции повторно и в других своих программах.
# Организуем свою библиотеку функций.
# В корне вашего проект создайте папку Library(это будет пакет)
# В папке Library создайте файл my_lib.py(это и будет ваш библиотечный файл)
# Все функции разместите в файле my_lib.py
# Решения всех задач, использующих ваши функции, разместите в отдельном(отдельных - на ваше усмотрение) файле(файлах),
# а используемые функции импортируйте из my_lib.py
import random

def gen_list(size=10, of=1, to=10):
    rand_list=[]
    for i in range(size):
        rand_list.append(random.randint(of, to))
    return rand_list

def palindrome(number):
    revers=0
    num=number
    while number:
        revers=revers*10+number%10
        number//=10
    return revers==num

def pagination(num_items, items_on_page):
    num_pages=num_items//items_on_page+(num_items%items_on_page+items_on_page-1)//items_on_page

    return num_pages

def days_in_year(num_year):
    return num_year%4==0 and not(num_year%400==0)
