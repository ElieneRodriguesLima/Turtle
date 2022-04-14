import turtle
  
t=turtle.Turtle()
t.shape("turtle")
t.speed(3)
t.fillcolor("pink")
menor = 100
maior = 5 * menor

for i in range(4):
    if(i % 2 == 0):
        t.fd(maior)
    if(i % 2 == 1):
        t.fd(menor)
    t.lt(90)
   


