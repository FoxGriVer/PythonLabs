from turtle import *

def draw_square():
    i = 0
    j = 9
    iteration = 1

    while(iteration < j):
        for iteration in range(1, j):
            while (i < 4):
                forward(30)
                right(90)
                i += 1
            forward(30)
            i = 0
        j -= 1
        iteration = 1
        backward(30 * j)
        if(j != 1):
            left(90)
            forward(30)
            right(90)

# draw_square()

# input()