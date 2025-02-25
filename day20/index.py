from turtle import  Screen,Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("blue")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# for each_position in stating_position:
#     my_segment = Turtle("square")
#     my_segment.color("white")
#     my_segment.goto(each_position)
#     segments.append(my_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0,1)

    snake.move()

    # for each_segment in range(len(segments) - 1, 0, -1):
    #     new_x = segments[each_segment- 1].xcor ()
    #     new_y= segments[each_segment- 1].ycor()
    #     segments[each_segment].goto(new_x, new_y)
    #     # each_segment.forward(20)
    # segments[0].forward(20)


screen.exitonclick()



















screen.exitonclick()
