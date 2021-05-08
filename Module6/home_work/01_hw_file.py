# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла


def log(text, file="log.txt"):
    with open("data/"+file, "a", encoding="utf-8") as f:
        f.write(text)
    return 0


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
