# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
from random import randint
# Создаем 3 кортежа случайных чисел, используя списки
n=20
lst1=[]
lst2=[]
lst3=[]
for i in range(n):
    lst1.append(randint(1,10))
    lst2.append(randint(1,10))
    lst3.append(randint(1,10))
tup_lst1=tuple(lst1)
tup_lst2=tuple(lst2)
tup_lst3=tuple(lst3)
print(tup_lst1)
print(tup_lst2)
print(tup_lst3)
# Объединенное множество из элементов всех трех кортежей
set_sum=set(tup_lst1+tup_lst2+tup_lst3)
count=0
lst_cross=[]
# Проходим по множеству и для каждого элемента считаем минимальное кол-во вхождений в трех кортежах
for i in set_sum:
    min_count=min(tup_lst1.count(i),tup_lst2.count(i),tup_lst3.count(i))
# Если вхождений больше нуля, то увеличиваем счетчик на эту величину
# и столько же раз добавляем этот элемент множества в результирующий список вхождений
    if min_count>0:
       count+=min_count
       for _ in range(min_count):
           lst_cross.append(i)
print(count,lst_cross)
