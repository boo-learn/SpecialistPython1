# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
     with open(name_file, 'a') as file:
          file.write(text)

if __name__ =='__main__':
    log('hello world')
    log('message', 'log01.txt')
