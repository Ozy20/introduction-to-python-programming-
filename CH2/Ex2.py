import math
print("Enter the radius and length of a cylinder:")
radius = eval(input())
length = eval(input())
area = radius * radius * math.pi
volume = area * length
print("the area is ",area)
print("the volume is ",volume)
