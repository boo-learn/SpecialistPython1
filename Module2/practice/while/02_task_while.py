# Напишите программу, которая запрашивает строку до тех пор, пока пользователь не введет “хватит”.
# Т.е. программа запрашивает ввод, если вводится любое значение отличное от слова “хватит”,
# то программа запрашивает ввод снова.

# TODO: your code here
msg = ''
while msg != "хватит":
    msg = input("Напиши слово 'хватит' или это будет продолжаться снова и снова ")
    print(msg)
