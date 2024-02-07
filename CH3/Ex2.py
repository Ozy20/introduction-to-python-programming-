import math

print("enter point 1")
x1 = eval(input())
x1 = math.radians(x1)
y1 = eval(input())
y1 = math.radians(y1)
print("enter point 2")
x2 = eval(input())
x2 = math.radians(x2)
y2 = eval(input())
y2 = math.radians(y2)
d=6371.01 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(y1) * math.cos(y2) * math.cos(y1-y2))
print("The distance between the two points is",d)
