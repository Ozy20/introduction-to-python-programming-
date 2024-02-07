import math
sin = 0
cos = 0
degree = 0
print("Degree       sin         cos")
while degree <= 350:
    sin = round(math.sin(math.radians(degree)), 4)
    cos = round(math.cos(math.radians(degree)), 4)
    degree += 10
    print(f"{degree:4}     {sin:7}     {cos:7}")
