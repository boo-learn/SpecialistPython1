# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here

n = int(input ("Please enter num: "))

if n % 3 == 0 and n % 5 == 0:
  print ("Foobar")
elif n % 3 == 0:
  print ("Foo")
elif n % 5 == 0
  print ("Bar")
