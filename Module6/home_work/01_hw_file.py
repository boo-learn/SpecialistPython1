# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

import os

def log(text, file="log.txt", path="data"):
    # fullname = path + "/" + file
    fullname = os.path.join(path,file)
    with open(fullname,"a", encoding="utf-8") as f:
        print(text, file = f)

log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
