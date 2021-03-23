def palindrome(number):
    reverse = 0
    number_init = number
    while number > 0:
        dig = number % 10
        reverse = reverse * 10 + dig
        number = number // 10
    return reverse == number_init
a = 9
b = 33
palindrome_count = 0
for i in range(a, b + 1):
    if palindrome(i):
        palindrome_count +=1
print(palindrome_count)           #4
