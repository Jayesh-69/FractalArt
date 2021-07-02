import turtle
import random

turtle.speed(0)

for _ in range(1500):
    turtle.forward(5)
    temp = random.randint(0, 2)
    if temp == 0:
        turtle.left(90)
    elif temp == 1:
        turtle.right(90)
    else:
        turtle.left(0)

turtle.mainloop()
