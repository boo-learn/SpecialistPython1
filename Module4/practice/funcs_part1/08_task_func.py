# Напишите функцию находящую n-ое число Фибоначчи.
seq = [1,1]
def fibo (n):
    for i in range (2,n):
        seq.append (seq[i-2]+seq[i-1])
    return(seq[i])
