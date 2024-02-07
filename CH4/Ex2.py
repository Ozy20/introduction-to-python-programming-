import random
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
print(a,"+",b,"+",c,"=?")
ans=eval(input())

if (a + b + c) == ans:
   print("your answer is correct")
else:
    print("your answer is wrong")
    
               
