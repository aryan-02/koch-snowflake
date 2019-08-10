import turtle

shape = "FRFRF" # Initial Condition, Equilateral Triangle
iterations = 9

for i in range(iterations): # Iteratively build the instructions to make the Koch Snowflake
	# Replace ____ with _/ \_
	shape = shape.replace("F","FLFRFLF")

turtle.speed(0) # Avoid turtle moving animations
turtle.ht() # Hide Turtle

# Bring the turtle to an initial position such that the shape is visible on the screen
turtle.pu()
turtle.bk(400)
turtle.lt(90)
turtle.fd(200)
turtle.rt(90)
turtle.pd()

# Parse and execute the instructions to make the snowflake
for ins in shape:
	if ins == "F":
		turtle.fd(200.0 / (3 ** (iterations - 1)))
	elif ins == "L":
		turtle.lt(60)
	elif ins == "R":
		turtle.rt(120)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="koch_flake.eps")

input() # Wait for user input