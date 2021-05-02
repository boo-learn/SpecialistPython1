# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tup1=4,6,8,10
tup2=4,6
tup3=4,6,8,11,12,1
counter=0
for e in tup1:
    if tup2.count(e)!=0 and tup3.count(e)!=0:
        counter+=max(tup2.count(e), tup3.count(e))
print(counter)
