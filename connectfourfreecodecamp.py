##Connect Four from FreeCodeCamp
##random number generators typically used in AI's connect four
##ratios
#convert typical gameplay into value
#scoring mechanism: center, lines of two, lines of three
##offense and defense
#opp line of two, opp winnable line of three
#AI's moves are based off what move has the most value (points)						  x	]
##chess: taking, losing pieces, piece strength, piece positioning, [x, x, x, x, x, x, x
															#      [x
##Variables: positions(row count, column count), spaces(even, odd)
import turtle
import os


#create a window
wn = turtle.Screen()
wn.title("Pong by Me (TokyoEdTech)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



# Function to move the paddles
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
	

#Keyboard Biinding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "e")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "i")
	
#main game loop
while True:
	wn.update()
	
	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	#Border Checking
	
	# Top and Bottom
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

		
	elif ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		
	# Left and right
	if ball.xcor() > 350:
		score_a += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=
		("Courier", 24, "normal"))
		ball.goto(0, 0)
		ball.dx *= -1
		
	elif ball.xcor() < -350:
		score_b += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=
		("Courier", 24, "normal"))
		ball.goto(0, 0)
		ball.dx *= -1

	# Paddle and ball collisions
	if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.dx *= -0.5
		
		
	elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.dx *= -0.5
		
