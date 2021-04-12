# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

num = int(input("your number:"))
if  num%5 == 0 and num%3 == 0:
    print("Foobar")
elif num%5 == 0:
    print("Bar")
elif  num%3 == 0:
    print("Foo")
else:
    print( )
