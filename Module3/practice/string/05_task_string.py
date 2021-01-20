# Вам дана строка, состоящая из строчных латинских букв и пробелов.
# Ваша задача — определить, является ли эта строка «перевертышем», если удалить из нее все пробелы и знаки пуктуации.
# Строка называется «перевертышем», если читается одинаково слева направо и справа налево.

str = 'И темен город Мороз узором дорог не мети'

new_str = str.lower()
print(new_str)
words = new_str.split()

i = 0
converted_str = ''
while i < len(words):
    converted_str += words[i]
    i += 1
  
converted_str_2 = converted_str[::-1]
print(converted_str_2)
if converted_str == converted_str_2:
    print('Перевёртыш')


