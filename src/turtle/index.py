# python src/turtle/index.py
import turtle as t

# Start
t.shape("turtle")

# Equilateral Triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120) # 외각의 각도

# Circle
t.circle(50) # Radius

# Quadrilateral (slanted)
t.circle(40, steps=4) # Radius, Steps

# Pen Setting
t.pensize(5)
t.color("red")

# Quadrilateral
for i in range (4):
    t.forward(100)
    t.left(90)
    
# Pen Setting
t.pensize(1)
t.color("purple")

# Regular Pentagon
t.begin_fill()
n = 5
for x in range (n):
    t.forward(50)
    t.left(360/n)
t.end_fill()

# End
t.hideturtle()
t.done()
