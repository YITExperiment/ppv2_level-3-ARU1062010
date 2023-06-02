import turtle as t
def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin-fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
     t.end-fill()
     t.penup()

    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')

    #feet
    t.goto(=100, =150)
    rectangle(50,20,'biue')
    t.goto(=30,=150)
    rectangle(50,20,'biue')

    #legs
    t.goto(-25,-50)
    rectangle(15,100,'grey')
    t.goto(-55,-50)
    rectangle(-15,100,'grey)
     
