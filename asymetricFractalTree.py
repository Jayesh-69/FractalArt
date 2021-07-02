import turtle

# This method will draw the tree
turtle.speed(0)


def tree(size, levels):
    if levels <= 0:
        # turtle.color("green")
        # turtle.penup()
        # turtle.forward(10)
        # turtle.dot(size)
        # turtle.backward(10)
        # turtle.pendown()
        # turtle.color("black")
        return

    turtle.forward(size)
    turtle.right(70)
    tree(size*0.7, levels-1)

    turtle.left(100)
    tree(size*0.7, levels-1)

    turtle.right(30)
    turtle.backward(size)


turtle.left(90)  # we are doing this so that our tree will be standing
# Follwing code will make the position of tree a bit down so that our tree will not be in centre
turtle.penup()
turtle.backward(150)
turtle.pendown()
# now we can draw the tree
tree(110, 9)

turtle.mainloop()  # This will make the program run until we close the window.
