from turtle import Turtle, Screen


def hexagon(turta, hexa_color, border_color):
    turta.up()
    turta.goto(-200, 0)
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

    turta.home()
    turta.end_fill()


def main():
    t = Turtle()
    wind = Screen()
    hexa_color = input("Enter a hexagon color: ")
    border_color = input("Enter a border color: ")
    hexagon(t, hexa_color, border_color)
    wind.mainloop()


main()
