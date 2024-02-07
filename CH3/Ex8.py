amount = eval(input("Enter the amount: "))
amount *= 100
amount = int(amount)
num_of_dollers = amount // 100
num_of_cents = amount % 100
print(amount," represents ",num_of_dollers,"dollers and ",num_of_cents," cents")
