# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла
from pathlib import Path

def log(text, file="log.txt"):
    logged_string = str(text)

    if logged_string.strip() == "":
        return

    log_file = Path(file)
    mode = "a" if log_file.is_file() else "w"

    with open(file, mode, encoding="utf-8") as f:
        f.write(logged_string + "\n")


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
