#   a117_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
#makes horizontal turtles and add to the list
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
#make vertical turtles and adto the list
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 50:
    steps = steps + 1

    for h_turtle in horiz_turtles:
        for v_turtle in vert_turtles:

            h_turtle.forward(10)
            v_turtle.forward(10)

            x1 = h_turtle.xcor()
            x2 = v_turtle.xcor()

            y1 = h_turtle.ycor()
            y2 = v_turtle.ycor()

            if abs(x1-x2)< 20 and abs(y1-y2)<20:
                h_turtle.fillcolor("gray")
                v_turtle.fillcolor("gray")
    
                horiz_turtles.remove(h_turtle)
                vert_turtles.remove(v_turtle)
    
wn = trtl.Screen()
wn.mainloop()