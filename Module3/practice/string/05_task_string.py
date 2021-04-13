# Вам дана строка, состоящая из строчных латинских букв и пробелов.
# Ваша задача — определить, является ли эта строка «перевертышем», если удалить из нее все пробелы и знаки пуктуации.
# Строка называется «перевертышем», если читается одинаково слева направо и справа налево.

# Пример строки перевертыша: "И темен город. Мороз узором дорог не мети."
text = input('Строка: ')
text = text.replace(' ', '')
text_replace = text
for i in range(len(text)):
    if not text[i].isalpha():
        text_replace = text.replace(text[i], '')

text_revers = text_replace[::-1]

if text_revers.lower() == text_replace.lower():
    print('Перевертыш')
else:
    print('Не перевертыш')
