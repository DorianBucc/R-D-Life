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

# Répéter le flocon avec tailles croissantes, en descendant
for i in range(1, 10):
    size = (i / 2) * 60
    t.penup()
    t.goto(-size / 2, 200 - i * 50)  # Centrage horizontal, descente verticale
    t.setheading(0)  # Réinitialiser l'orientation vers la droite
    t.pendown()
    
    for _ in range(3):
        koch(t, order=2, size=size)
        t.right(120)

window.exitonclick()
