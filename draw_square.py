import turtle

# draw a circle with 36 squares...360 degrees

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    
    #Create turtle, draws a square.
    nick = turtle.Turtle()
    nick.shape("turtle")
    nick.color("blue")
    nick.speed(4)
    for i in range(1,37):
        draw_square(nick)
        nick.right(10)

    #Create turtle Angie, draws a circle.
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()


draw_art()
