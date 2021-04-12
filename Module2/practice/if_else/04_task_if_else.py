# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here

number = int(input())
string = ""
if number % 3 == 0:
	string = "Foo"
if number % 5 == 0:
	string = string + "Bar"

print(string)
