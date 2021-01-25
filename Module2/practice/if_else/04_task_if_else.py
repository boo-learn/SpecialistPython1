# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

number = int(input("введите целое число"))

if number%5 ==0 and number%5 == 0:
    print("Foobar")
elif number%3 == 0:
    print("Foo")
elif number%5 and number%5 == 0:
    print("Bar")
