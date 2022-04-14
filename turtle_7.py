import turtle

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("pink")
t.speed(5)


def quadrado(quadrado):
     for q in range(4):
          t.forward(quadrado)
          t.left(90)

for q in range(8):
    quadrado(90+q*20)

