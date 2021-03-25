# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt", path="data"):
    fullname = path + "/" + file
    with open(fullname, "a") as task:
        print(text, file=task)


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
