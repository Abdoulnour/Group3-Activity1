from turtle import Turtle, Screen

def draw_circle(turta, x,y,radius,color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
def draw_nose(turta,x,y,radius,color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
def draw_eye1(turta,x,y,radius,color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
def draw_eye2(turta,x,y,radius,color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()

def mouth(turta,x,y,radius,color):
     turta.up()
     turta.goto(x,y)
     turta.down()
     turta.begin_fill()
     turta.fillcolor(color)
     turta.circle(radius,180)
     turta.end_fill()

def main():
    t=Turtle()
    wind= Screen()
    draw_circle(t,0,0,200,"yellow")
    draw_nose(t,0,140,30,"red")
    draw_eye1(t,-70,250,30,"blue")
    draw_eye2(t,70,250,30,"blue")
    mouth(t,50,50,50,"black")
main()