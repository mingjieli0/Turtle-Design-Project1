import turtle

turtle.speed(0)

def draw(n):
    for i in range(5):
        turtle.forward(80)
        turtle.left(n)
for i in range(1500):
    draw(36*(i+1.0016))
