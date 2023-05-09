import tkinter as tk
import random as rnd
import turtle
import time

window = tk.Tk()
window.geometry("500x500")
window.title("Fantaci")
canvas = tk.Canvas(window,bg="white",width=500,height=500)
canvas.place(x=0,y=0)
colors =["red","blue","green","pink","black","yellow","orange","purple","brown"]
yeas = "yeas"
no = "no"

def random_button():   
    def pentogon():
        for i in range(4):
            pencil.forward(rnd.randint(20,100))
            pencil.left(rnd.randint(20,100)) 

def circle():
    color = rnd.choice(colors)
    d = rnd.randint(1,100)
    x = rnd.randint(0,500-d)
    y = rnd.randint(0,500-d)
    canvas.create_oval(x,y,x+d,y+d,fill=color) 

def oval():
    color = rnd.choice(colors)
    d1 = rnd.randint(1,100)
    d2 = rnd.randint(1,100)
    x = rnd.randint(0,500-d1)
    y = rnd.randint(0,500-d2)
    canvas.create_oval(x,y,x+d1,y+d2,fill=color)    

def square():
    color = rnd.choice(colors)
    color_border = rnd.choice(colors)
    d = rnd.randint(1,100)
    x = rnd.randint(0,500-d)
    y = rnd.randint(0,500-d)
    canvas.create_rectangle(x,y,x+d,y+d,fill=color,outline=color_border)

def crazy_circles():
    while True:
        circle()
        window.update()

def story():
    stranger  = input("Hi.Would you like go on adventure?")
    if stranger == yeas:
        stranger = input("Good.Now lets get get going.We hit the wolf pack. I think we need to run! ")
        if stranger == yeas:
                   print("You wake up that was a nightmare. You now after plaing 'Guess number'!!")
        else:
             stranger = input("The men who was with you run but they were gust hungry.You gave them meat and pet them.The alptha don't like you.His name is,Deth.Oh no.Run now!!")
             if stranger == yeas:
                print("You try to run but he,is,to,fast!")
             else:
                 stranger = input("You want to figth him?")
                 if stranger ==  yeas or no:
                     print("You died in dream.And in real life.:(")
    if stranger == no:
        stranger = input("Ok.You walk and hit the park.You want to go in or pass buy.")

def pink_ponk():
    color = rnd.choice(colors)
    d = rnd.randint(1,100)
    x = rnd.randint(0,500-d)
    y = rnd.randint(0,500-d)
    circle = canvas.create_oval(x,y,x+d,y+d,fill=color)
    dx = 2
    dy = 2
    while True:
        cords = canvas.coords(circle)
        left = cords[0]
        top = cords[1]
        right = cords[2]
        down = cords[3]
        if left <= 0 or right >= 500:
            dx = -dx
        if top <= 0 or down >= 500:
            dy = -dy
        canvas.move(circle,dx,dy)
        time.sleep(0.01)
        window.update()

pencil = turtle.Turtle()
pencil.speed(1)
pencil.shape("turtle")
pencil.color("red")


label = tk.Label(window,text = "Click the button to see what they do",bg="light green")
label.place(x=150,y=0)
circle_button = tk.Button(window,text="Draw circle",bg="red",command=circle)
circle_button.place(x=0,y=100)
square_button = tk.Button(window,text="Square club",bg="blue",command=square)
square_button.place(x=0,y=250)
oval = tk.Button(window,text="Draw oval",bg="orange",command=oval)
oval.place(x=0,y=125)
crazy_circle = tk.Button(window,text="Click and see",bg="yellow",command=crazy_circles)
crazy_circle.place(x=0,y=150)
pink_ponk = tk.Button(window,text="Play pink ponk",bg="green",command=pink_ponk)
pink_ponk.place(x=0,y=175)
special_fetures = tk.Button(window,text="???",bg="light blue",command=random_button)
special_fetures.place(x=0,y=200)
story_button = tk.Button(window,text="Story time",bg="purple",command=story)
story_button.place(x=0,y=225)

window.mainloop()
