from turtle import Turtle, Screen
"""AbdoulNour, Zayed shatat, Sama Nimer"""

def circle(turta, circle_color, border_color):
    turta.pencolor(border_color)
    turta.pensize(3)
    turta.begin_fill()
    turta.fillcolor(circle_color)
    turta.circle(50)
    turta.end_fill()
   
    turta.up()
    turta.goto(-110, 125)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(circle_color)
    turta.circle(50)
    turta.end_fill() 

    turta.up()
    turta.goto(110, -125)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(circle_color)
    turta.circle(50)
    turta.end_fill()

def square(turta, square_color, border_color):
    turta.pencolor(border_color) 
    turta.pensize(3) 
    turta.up()
    turta.goto(110,0)
    turta.down()
    turta.begin_fill() 
    turta.fillcolor(square_color)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()

    turta.up()
    turta.goto(0,125)
    turta.down()
    turta.begin_fill() 
    turta.fillcolor(square_color)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()

    turta.up()
    turta.goto(200,-125)
    turta.down()
    turta.begin_fill() 
    turta.fillcolor(square_color)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()


def hexagon(turta, hexa_color, border_color):
    turta.up()
    turta.goto(-150,0)
    turta.pensize(3)
    turta.down()
    turta.begin_fill()
    turta.color(hexa_color)
    turta.pencolor(border_color)
    
    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)
    turta.up()
    turta.home()
    turta.end_fill()

    turta.up()
    turta.goto(-250,125)
    turta.down()
    turta.begin_fill()
    turta.color(hexa_color)
    turta.pencolor(border_color)
    
    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)
    turta.up()
    turta.home()
    turta.end_fill()

    turta.up()
    turta.goto(-50,-125)
    turta.down()
    turta.begin_fill()
    turta.color(hexa_color)
    turta.pencolor(border_color)
    
    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)
    turta.up()
    turta.home()
    turta.end_fill()
    


def pattern(turta, hexa_color, circle_color, square_color, border_color):
    circle_color = input("Enter a circle color: ")
    square_color = input("Enter a square color: ")
    hexa_color = input("Enter a hexagon color: ")
    border_color = input("Enter a border color: ")

    circle(turta,circle_color,border_color)
    square(turta, square_color, border_color)
    hexagon(turta,hexa_color, border_color)



def main():
    t=Turtle()
    wind=Screen()
    pattern(t, "hexa_color", "circle_color", "square_color", "border_color")
    wind.bgcolor("light blue")
    wind.exitonclick()
    
    
   

main()