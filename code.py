import random
import turtle as trtl


apple_image = "apple.gif"  
pear_image = "pear.gif"  

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")  
wn.addshape(apple_image)  
wn.addshape(pear_image)  


apple = trtl.Turtle()


def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()


def draw_pear(active_pear):
    active_pear.shape(pear_image)
    wn.update()


letters = ["a", "s", "d", "f"]


def apple_turtles(letters):
    turtles = []
    for _ in letters:
        t = trtl.Turtle()
        t.penup()
        draw_apple(t)
        t.goto(random.randint(-100, 100), random.randint(-10, 90))  
        turtles.append(t)
    return turtles


def draw_letters(letters, turtles):
    drawers = []  
    for i in range(len(turtles)):
        drawer = trtl.Turtle()  
        drawer.penup()
        drawer.hideturtle()  
        turtle = turtles[i]
        drawer.goto(turtle.xcor() - 18, turtle.ycor() - 35)  
        drawer.write(letters[i], font=("Arial", 40, "bold"))  
        drawers.append(drawer) 
    return drawers

def a_pressed():
    print("A key pressed")
    index = 0
    apple_fall(index)
    erase_letter(index)

def s_pressed():
    print("S key pressed")
    index = 1
    apple_fall(index)
    erase_letter(index)

def d_pressed():
    print("D key pressed")
    index = 2
    apple_fall(index)
    erase_letter(index)

def f_pressed():
    print("F key pressed")
    index = 3
    apple_fall(index)
    erase_letter(index)


def apple_fall(index):
    global turtles  
    apple = turtles[index]  
    x = apple.xcor()
    y = apple.ycor()
    apple.goto(x, y - 140)  


def erase_letter(index):
    global drawers  
    drawer = drawers[index]  
    drawer.clear() 


turtles = apple_turtles(letters)  
drawers = draw_letters(letters, turtles)  


wn.onkeypress(a_pressed, "a")
wn.onkeypress(s_pressed, "s")
wn.onkeypress(d_pressed, "d")
wn.onkeypress(f_pressed, "f")

wn.listen()  
wn.mainloop()  
