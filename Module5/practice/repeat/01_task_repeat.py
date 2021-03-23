# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    import random
    mylist = []
    i=0
    while i<=size:
        element = random.randrange(of,to)
        mylist.append(element)
        i= i+1
    return mylist

print (gen_list(10,0,100))
