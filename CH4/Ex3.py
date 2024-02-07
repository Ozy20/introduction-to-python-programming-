a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
d = float(input("enter d: "))
e = float(input("enter e: "))
f = float(input("enter f: "))
den = (a * d) - (b * c)
if den == 0 :
    print("the equation has no solution")
else:
    print("x = ",((e * d) - (b * f)) / den," y = ",((a * f) - (e * c)) / den)
