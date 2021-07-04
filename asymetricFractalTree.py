import turtle

# This method will draw the tree
turtle.speed(0)


def tree(size, levels):
    if levels <= 0:
        return
    if levels <= 3:
        turtle.color("green")
    else:
        turtle.color("brown")

    turtle.forward(size)
    turtle.right(70)
    tree(size*0.7, levels-1)

    turtle.left(100)
    tree(size*0.7, levels-1)

    turtle.right(30)
    turtle.penup()
    turtle.backward(size)
    turtle.pendown()


turtle.left(90)  # we are doing this so that our tree will be standing
# Follwing code will make the position of tree a bit down so that our tree will not be in centre
turtle.penup()
turtle.backward(300)
turtle.pendown()
# now we can draw the tree
tree(200, 5)

turtle.mainloop()  # This will make the program run until we close the window.
