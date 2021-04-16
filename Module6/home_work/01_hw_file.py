# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    logged_string = str(text)

    if logged_string.strip() == "":
        return

    with open(file, "a", encoding="utf-8") as f:
        f.write(logged_string + "\n")


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
