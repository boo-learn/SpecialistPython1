text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

i = 0
j = 0
long_word = 0

while i < len(text):
    if text[i] != ' ':
        j += 1
    elif j > 5:
        long_word += 1
        if text[i] == ' ':
            j = 0
    else:
        j = 0

    i += 1

print ('There is ', long_word, 'words in this text, that are longer then 5 letters')
