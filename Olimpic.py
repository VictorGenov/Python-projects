import turtle

pencil = turtle.Turtle()
pencil.color("blue")
pencil.speed(10)

def circle():
    for i in range(60):
        pencil.forward(5)
        pencil.left(6)

def move(x,y):           
    pencil.up()
    pencil.goto(x,y)
    pencil.down()
    
##def olimpic_rings(x,y,color):
##    pencil.color(color)    
##    pencil.width(9)
##    move(x,y)
##    circle() 
##olimpic_rings(-120,60,"blue")
##olimpic_rings(0,60,"black")
##olimpic_rings(-60,0,"yellow")
##olimpic_rings(60,0,"green")
##olimpic_rings(120,60,"red")

def up():
    pencil.setheading(90)
    pencil.forward(10)
def left():
    pencil.setheading(180)
    pencil.forward(10)
def down():
    pencil.setheading(-90)
    pencil.forward(10)
def right():
    pencil.setheading(0)
    pencil.forward(10)
def pen_up():
    pencil.up()
def pen_down():
    pencil.down()

##pen_down()
##pen_up()
right()    
down()
left()
up()
pencil.screen.onkeypress(up,"Up")
pencil.screen.listen()
pencil.screen.onkeypress(left,"Left")
##pencil.screen.listen()
pencil.screen.onkeypress(down,"Down")
##pencil.screen.listen()
pencil.screen.onkeypress(right,"Right")
##pencil.screen.listen()
pencil.screen.onkeypress(pen_up,"w")
pencil.screen.onkeypress(pen_down,"s")

pencil.screen.mainloop()
