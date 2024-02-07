import random

x = random.randint(0,100)
y = random.randint(0,100)
print(x,"+",y,"?")
z = eval(input())
if x + y == z:
   print("the answer is correct")
else:
   print("the answer is wrong")
