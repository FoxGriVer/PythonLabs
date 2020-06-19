from turtle import *

def draw_picture(filename, size = 10):
    pensize(2)
    colormode(255)
    tracer (0, 0)
    # delay (0)

    with open(filename, "r") as rgbFile:
        positionX = 0

        for line in rgbFile:

            listOfRGBTuples = list()

            rbgLine = line.split()

            for rbgColor in rbgLine:
                listOfRGBTuples.append(tuple(map(int, rbgColor[1:-1].split(','))))
            
            for currentColor in listOfRGBTuples:

                penup()
                begin_fill()

                pencolor(currentColor)
                fillcolor(currentColor)
                right(90)
                forward(size)
                right(90)
                forward(size)
                right(90)
                forward(size)
                right(90)
                forward(size)
                right(90)
                forward(size)
                left(90)

                end_fill()

            positionX += size
            setx(positionX)
            sety(0)

    done()

draw_picture("C:/Users/MacPavel/Desktop/pythonLabs/lab9/secret_picture.txt", 2)
