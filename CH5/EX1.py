x = eval(input("Enter a num: "))
Sum = x
count = 0
average = Sum
while x > 0:
    x = eval(input("Enter a num: "))
    Sum += x
    count += 1
    average = Sum / count
print("sum is "+str(Sum)+" average is "+str(average))
