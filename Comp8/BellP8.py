#BellP8
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency with turtle graphics

import turtle

def draw_triangle(vertices, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for vertex in vertices:
        turtle.goto(vertex)
    turtle.goto(vertices[0])  # Close the triangle
    turtle.end_fill()

def sierpinski(vertices, depth):
    colors = ["blue", "green", "red", "purple", "orange"]
    draw_triangle(vertices, colors[depth % len(colors)])
    
    if depth > 0: #
        # Notes:
            #Formally: Each midpoint is the average of two given points
            #Ergo, The midpoint of Points (a,b) and (x,y) should equal (avg{a,x} , avg{b,y})  (syntactically invalid, for demo only)
        mid1 = ((vertices[0][0] + vertices[1][0])/2 , (vertices[0][1] + vertices[1][1])/2)
        #Explode(       a       +       x       )/2 , (         b     +         y       )/2 
        mid2 = ((vertices[1][0] + vertices[2][0])/2 , (vertices[1][1] + vertices[2][1])/2)
        mid3 = ((vertices[2][0] + vertices[0][0])/2 , (vertices[2][1] + vertices[0][1])/2)
        
        sierpinski([vertices[0], mid1, mid3], depth - 1)
        sierpinski([mid1, vertices[1], mid2], depth - 1)
        sierpinski([mid3, mid2, vertices[2]], depth - 1)

def main():
    turtle.speed(0)
    turtle.penup()
    
    screen = turtle.Screen()
    screen.bgcolor("white")
    size = int(consolizeSizeInput()) #Get size from user
    start_x, start_y = (-size/2, -size/2) #Dynamically handle startpoint based on user input
    vertices = [(start_x, start_y), (start_x + size, start_y), (start_x + size / 2, start_y + size * 0.866)]
    
    sierpinski(vertices, consolizeDepthInput())  #Get recursion depth from user
    
    turtle.hideturtle()
    turtle.done()
    
def consolizeDepthInput(): #actually handle getting the depth from the user
    depth = int(input("""How many recurrences do you want in your triangle?
                                   
                                   
Note: Hardware limitations require I suggest you keep
this number below 7, but like, do what you want, it's
your CPU and RAM you'll be cooking.

Recursions:  """))
    return depth



def consolizeSizeInput(): #actually handle getting the size from the user
    size = int(input("What size (in px) would you like your triangle to be?  "))
    return size

if __name__ == "__main__":
    main()
