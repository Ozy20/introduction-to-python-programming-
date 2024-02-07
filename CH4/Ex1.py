import math

a = eval(input("enter a: "))
b = eval(input("enter b: "))
c = eval(input("enter c: "))
dis = pow(b,2)-(4*a*c)

if dis > 0:
    print("r1 = ",(-b + math.sqrt(dis)) / (2 * a),", r2 = ",(-b - math.sqrt(dis)) / (2 * a))
elif dis == 0:
    print("r = ",(-b + math.sqrt(dis)) / (2 * a))
else:
    print("the equation has no solutions")
    
