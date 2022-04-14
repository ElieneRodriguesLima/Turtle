import turtle

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("pink")
t.speed(5)


def quadrado():
     for i in range(4):
          t.forward(100)
          t.left(90)

quadrado()
t.penup()
t.forward(200)
t.pendown()
quadrado()

quadrado()
t.penup()
t.forward(200)
t.pendown()
quadrado()









