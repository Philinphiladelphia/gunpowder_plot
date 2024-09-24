from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor('lightblue')

spaceship = Turtle()
spaceship.color('red')
spaceship.penup()

speed = 10

def travel():
    if not engine.is_on():
        print("Engine's off!")
    else:
        print("Ship at: " + str(spaceship.pos()))

        ## send coords to ROS

        spaceship.forward(speed)

    wn.ontimer(travel, 50)


class Engine:
    engine_on = True
    def toggle_engine(self):
        self.engine_on = not self.engine_on
    def is_on(self):
        return self.engine_on

engine = Engine()

wn.onkey(lambda: spaceship.setheading(90), 'Up')
wn.onkey(lambda: spaceship.setheading(180), 'Left')
wn.onkey(lambda: spaceship.setheading(0), 'Right')
wn.onkey(lambda: spaceship.setheading(270), 'Down')

wn.onkey(lambda: engine.toggle_engine(), 'space')

wn.listen()

travel()

wn.mainloop()