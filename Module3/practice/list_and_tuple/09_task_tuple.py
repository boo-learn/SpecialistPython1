# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tup1 = (1, 3, 4)
tup2 = (1, 1, 2, 3, 4, 5)
tup3 = (1, 1, 2, 4)

# 'simple' solution
print(len(set(tup1).intersection(set(tup2)).intersection(set(tup3))))

#'long' solution
# finding tuple with max length
max_tup_len = 0
max_tup = ()
for tup in tup1, tup2, tup3:
    if len(tup) > max_tup_len:
        max_tup_len = len(tup)
        max_tup = tup

# adding common elements to list
common_elem_list = []
for elem in max_tup:
    if elem in tup1 and elem in tup2 and elem in tup3 and elem not in common_elem_list:
        common_elem_list.append(elem)
print(len(common_elem_list))
