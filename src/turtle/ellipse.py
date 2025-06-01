# Ellipse (타원)
# python src/turtle/ellipse.py
import turtle
from math import sin, cos, pi

window = turtle.Screen()

# Style Setting
turtle.bgcolor("steelblue")
turtle.color("black")
turtle.fillcolor("red")
turtle.width(3)
turtle.speed(2)

# Start
turtle.begin_fill()

a = 300 #semi-major axis (장축)
b = 100 #semi-minor axis (단축)

turtle.penup()

for i in range(361):
    t = i*(pi/180) # 호도법 변환 공식 (세타)
    x = a*cos(t) # 타원 매개변수 방정식
    y = b*sin(t)
    turtle.goto(x, y)
    turtle.pendown()

# End
turtle.end_fill()
turtle.hideturtle()
turtle.done()








