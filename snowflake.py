import turtle


def create_snowflake(sides, length):
    for _ in range(sides):
        snowflake_side(length, sides)
        turtle.right(360/sides)


def snowflake_side(length, levels):
    if levels == 0:
        turtle.forward(length)
        return

    length /= 3.0
    snowflake_side(length, levels-1)
    turtle.left(60)

    snowflake_side(length, levels-1)
    turtle.right(120)

    snowflake_side(length, levels-1)
    turtle.left(60)

    snowflake_side(length, levels-1)


turtle.speed(0)
# Follwing code will align the pointer to upeer left conner so that the snowflake is in middle
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.pendown()
turtle.left(180)

# Here we give number of side and length for snowflake
create_snowflake(3, 100)

turtle.mainloop()
