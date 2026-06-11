import turtle
import time

t = turtle.Turtle()
t.fillcolor("blue")

# Start filling the shape
t.begin_fill()

# Side 1
t.forward(100)
t.left(72)
time.sleep(2) # 2 second delay

# Side 2
t.forward(100)
t.left(72)
time.sleep(2)

# Side 3
t.forward(100)
t.left(72)
time.sleep(2)

# Side 4
t.forward(100)
t.left(72)
time.sleep(2)

# Side 5
t.forward(100)
t.left(72)

# Complete the fill
t.end_fill()

turtle.done()