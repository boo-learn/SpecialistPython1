# Вам дана строка, состоящая из строчных латинских букв и пробелов.
# Ваша задача — определить, является ли эта строка «перевертышем», если удалить из нее все пробелы и знаки пуктуации.
# Строка называется «перевертышем», если читается одинаково слева направо и справа налево.

# Пример строки перевертыша: "И темен город. Мороз узором дорог не мети."

# TODO: your code here
text = input("text: ").lower()

for symb in [" ", ".", ",", "-", ":", ";", "?", '"', "(", ")", "!"]:
    text = text.replace(symb,"")

middle = int(len(text)/2)
is_palindrome = True
i = 0

while i <= middle:
    is_palindrome = is_palindrome and (text[i] ==text[-i-1])
    i += 1

print("Is palindrome!" if is_palindrome else "Not a palindrome")

