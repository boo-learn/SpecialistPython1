# Вам дана строка, состоящая из строчных латинских букв и пробелов.
# Ваша задача — определить, является ли эта строка «перевертышем», если удалить из нее все пробелы и знаки пуктуации.
# Строка называется «перевертышем», если читается одинаково слева направо и справа налево.

# Пример строки перевертыша: "И темен город. Мороз узором дорог не мети."

text = 'sator arepo tenet opera rotas'
text = text.replace(" ", "")
rev_text = ""

for c in text:
    rev_text = c + rev_text
if text == rev_text:
    print("Строка является перевертышем")
else:
    print("Строка не является перевертышем")
