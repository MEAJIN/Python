import turtle

def draw(w,y):
    t.goto(w,y)

t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)
s = turtle.Screen()
s.onscreenclick(t.goto)
