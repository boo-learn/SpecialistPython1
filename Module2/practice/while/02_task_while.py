# Напишите программу, которая запрашивает строку до тех пор, пока пользователь не введет “хватит”.
# Т.е. программа запрашивает ввод, если вводится любое значение отличное от слова “хватит”,
# то программа запрашивает ввод снова.

print('хватит - останавливает все')
a = ''

while a != 'хватит':
    a = input("Веди давай хоть что-нибудь: ")
