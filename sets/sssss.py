import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Zhwan in Pink with Floating Hearts")
screen.tracer(0)  # Turn off auto-update for animation

# Text turtle
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("deeppink")
text_turtle.goto(-100, 0)
text_turtle.write("zhwan", font=("Comic Sans MS", 48, "bold"))

# Heart class
class Heart(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("hotpink")
        self.penup()
        self.speed(0)
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
        self.setheading(random.randint(0, 360))
        self.shapesize(stretch_wid=0.5, stretch_len=0.8)
    
    def move(self):
        self.forward(2)
        if abs(self.xcor()) > 350 or abs(self.ycor()) > 350:
            self.goto(random.randint(-300, 300), random.randint(-300, 300))
            self.setheading(random.randint(0, 360))

# Create hearts
hearts = [Heart() for _ in range(20)]

# Animation loop
while True:
    for heart in hearts:
        heart.move()
    screen.update()
    time.sleep(0.02)
