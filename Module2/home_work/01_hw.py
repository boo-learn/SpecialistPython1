# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

print ("Input the demensions of the chocolate")
n = int(input("How many slices horizontally: "))
m = int(input("How many slices vertically: "))
k = int(input("How many slices do you want to break off: "))
if k%n==0 or k%m==0:
    print("YES")
else:
    print("NO")
