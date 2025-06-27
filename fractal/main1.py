import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch(t, order-1, size)
        t.left(60)
        koch(t, order-1, size)
        t.right(120)
        koch(t, order-1, size)
        t.left(60)
        koch(t, order-1, size)

# Création de la fenêtre et de la tortue
window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300, 90)
t.pendown()

# Répéter le flocon plusieurs fois, de plus en plus grand
for i in range(1, 10):
    size = (i / 2) * 60
    for _ in range(3):
        koch(t, order=2, size=size)
        t.right(120)
    t.penup()
    t.forward(size + 10)  # Espace entre les flocons
    t.pendown()

window.exitonclick()
