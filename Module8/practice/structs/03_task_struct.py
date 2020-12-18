# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random
random.seed(35)
def gen_list(size=20, of=1, to=5):
    rand_list=[]
    for i in range(size):
        rand_list.append(random.randint(of, to))
    return rand_list



lst=gen_list(20,-10,20)
print(lst)
count_under_10=len(list(filter(lambda el: el<=10, lst)))
print("Количество элементов больщих 10 ",count_under_10)
sum_positiv=sum(list(filter(lambda el: el>0, lst)))
print("Сумма положительных элементов ",sum_positiv)
lst_even=[lst[i] for i in range(0,len(lst),2)]
print ("Список четных элементов ",lst_even)
print("Среднее арифметическое четных элементов ",sum(lst_even)/len(lst_even))
