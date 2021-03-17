# Вам дана строка, состоящая из строчных латинских букв и пробелов.
# Ваша задача — определить, является ли эта строка «перевертышем», если удалить из нее все пробелы и знаки пуктуации.
# Строка называется «перевертышем», если читается одинаково слева направо и справа налево.

# Пример строки перевертыша: "И темен город. Мороз узором дорог не мети."

import re

text = "И темен город. Мороз узором дорог не мети."
text = text.replace(' ', '')
mirror = text[::-1]
print(text)
print(mirror)

text_no_punct = re.sub('[^\w\d\s]+', '', text)
mirror_no_punct = re.sub('[^\w\d\s]+', '', mirror)

if text_no_punct.lower() == mirror_no_punct.lower():
    print(text_no_punct)
    print(mirror_no_punct)
    print('Yes - mirrored')
else:
    print('No its different strings')
