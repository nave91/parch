import turtle

def tree(turt,line):
    if line > 0:
        turt.forward(line)
        turt.right(20)
        tree(turt,line-15)
        turt.left(40)
        tree(turt,line-15)
        turt.right(20)
        turt.backward(line)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.down()
    t.left(100)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(t,75)
    myWin.exitonclick()
        

main()
