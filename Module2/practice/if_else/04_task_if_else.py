# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

x = int(input("x:"))

if x % 3 == 0 and x % 5 == 0:
    print("Foobar")
elif x % 3 == 0:
    print("Foo")
elif x % 5 == 0:
    print("Bar")

