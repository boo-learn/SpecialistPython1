# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tup1 = (1,2,3)
tup2 = (1,3,5)
tup3 = (5,4,3,1)

cnt = 0
for t in tup1:
    if t in tup2 and t in tup3:
        cnt += 1
        print(t)

print("cnt: ", cnt)
