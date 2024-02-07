weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter weight in feet: "))
inches = eval(input("Enter weight in inches: "))
total_inches = feet * 12 + inches
weight_kilo = weight * 0.45359237
hieght_meters = total_inches * 0.0254
bmi = weight_kilo / (hieght_meters ** 2)
print("BMI is ",bmi)
if bmi < 18.5:
      print("Underweight")
elif bmi < 25:
      print("Normal")
elif bmi < 30:
      print("Overweight")
else:
      print("Obese")


