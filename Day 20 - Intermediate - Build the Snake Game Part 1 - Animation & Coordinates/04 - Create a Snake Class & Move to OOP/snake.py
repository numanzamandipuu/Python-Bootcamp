from turtle import Turtle

class Snake:

    tim_list = []

    for i in range(3):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(x=(-20 * i), y=0)
        tim_list.append(tim)


    def move(tim_list):

        for n in range(len(tim_list) - 1, 0, -1):
            new_x = tim_list[n - 1].xcor()
            new_y = tim_list[n - 1].ycor()
            tim_list[n].goto(new_x, new_y)

        tim_list[0].forward(20)

        if tim_list[0].xcor() > 280:
            game_is_on = False