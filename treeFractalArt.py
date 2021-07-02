import turtle

# This method will draw the tree


def tree(size, levels, angle):
    if levels == 0:
        turtle.color("green")
        turtle.penup()
        turtle.forward(10)
        turtle.dot(size)
        turtle.backward(10)
        turtle.pendown()
        turtle.color("black")
        return

    turtle.forward(size)
    turtle.right(angle)
    tree(size*0.8, levels-1, angle)

    turtle.left(angle*2)
    tree(size*0.8, levels-1, angle)

    turtle.right(angle)
    turtle.backward(size)


turtle.speed(0)  # to draw the tree as fast as possible
turtle.left(90)  # we are doing this so that our tree will be standing
# Follwing code will make the position of tree a bit down so that our tree will not be in centre
turtle.penup()
turtle.backward(150)
turtle.pendown()
# now we can draw the tree
tree(70, 5, 30)

turtle.mainloop()  # This will make the program run until we close the window.
