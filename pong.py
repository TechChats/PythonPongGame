
import turtle

#creating a turtle window
wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#for me when running this programs it shows 
#"ModuleNotFoundError: No module named 'tkinter'"
#so just install tkinter: sudo apt-get install python3-tk


# We need two paddles and a ball

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") 
# when we press w key the paddle_a_up functions calls and the left paddle moves up
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up") 
wn.onkeypress(paddle_b_down,"Down")
#Main game loop
while True:
    wn.update()
