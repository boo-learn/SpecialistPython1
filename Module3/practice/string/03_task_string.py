# Подсчитать количество букв «а» во введенной строке
string = input('Input your string: ')
count_a = string.count('a')
print('число букв а', count_a)
# Интересное дело, литера а бывает кириллической
str1 = 'напомни маме про раму'
count_a_cyr = str1.count('а')
count_a = str1.count('a')
print('count_a_cyr', count_a_cyr, '!= count_a', count_a)
