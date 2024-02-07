import turtle

length = eval(input("Enter length of the star: "))
turtle.forward(length)
turtle.setheading(216)
turtle.forward(length)
turtle.setheading(72)
turtle.forward(length)
turtle.setheading(288)
turtle.forward(length)
turtle.goto(0,0)
turtle.hideturtle()
