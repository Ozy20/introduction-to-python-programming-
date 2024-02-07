num = eval(input("Enter a 4-digits number: "))
Num = str(num % 10)
num //= 10
Num += str(num % 10)
num //= 10
Num += str(num % 10)
num //= 10
Num += str(num % 10)
print(Num)
