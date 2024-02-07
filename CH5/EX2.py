import random
num1 = 0
num2 = 0
count = 0
while count < 10:
    num1 = int(random.random() * 16)
    num2 = int(random.random() * 16)
    ANSWER = num1 + num2
    Q = eval(input("what is "+str(num1)+" + "+str(num2)+" ?"))
    if Q == ANSWER:
        print("your answer is correct ")
    else:
        print("your answer is wrong and corect answer is "+str(ANSWER))
    count += 1
         
        
    
