string_numbers = input("Enter numbers between 1 and 100: ")
numberslis = string_numbers.split()
numbers = [int(x)for x in numberslis]
numbers.sort()
xprev=-1
for x in numbers:
    if x != xprev: 
     print(str(x)+" occurs "+str(numbers.count(x))+" times")
     xprev=x
