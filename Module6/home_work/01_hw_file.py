# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    from os import path
    from settings import BASE_DIR

    f = open(path.join(BASE_DIR, "Files", file), "a", encoding="utf-8")
    f.write(f"{text}\n")


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
