from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import sys

x = 10
y = 10
right = False
left = True
top = True
bottom = False
sm = 1

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100,100,-100,100)

def square():
    global x
    global y
    #glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x-5, y-5.0)
    glVertex2f(x+5, y-5.0)
    glVertex2f(x+5, y+5.0)
    glVertex2f(x-5, y+5.0)
    glEnd()
    glutSwapBuffers()

def timer(t):
    #glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y
    global left
    global right
    global top
    global bottom
    global sm
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),timer,0)
    if x == 95.0:
        left = True
        right = False
        top = False
        bottom = False
    elif x == -95.0:
        right = True
        left = False
        top = False
        bottom = False
    elif y == 95.0:
        bottom = True
        top = False
        right = False
        left = False
    elif y == -95.0:
        top = True
        bottom = False
        right = False
        left = False

    if left == True:
        x-=0.5*sm
    elif right == True:
        x+=0.5*sm
    elif bottom == True:
        y-=0.5*sm
    elif top == True:
        y+=0.5*sm

def control(key,u,v):
    global x
    global y
    global right
    global left
    global top
    global bottom
    global sm
    if key == GLUT_KEY_LEFT:
        left = True
        right = False
        top = False
        bottom = False
    if key == GLUT_KEY_RIGHT:
        left = False
        right = True
        top = False
        bottom = False
    if key == GLUT_KEY_UP:
        top = True
        bottom = False
        right = False
        left = False
    if key == GLUT_KEY_DOWN:
        top = False
        bottom = True
        right = False
        left = False
    if key == GLUT_KEY_PAGE_UP:
        sm+=1
        if x == 95.0:
            left = True
            right = False
        elif x == -95.0:
            right = True
            left = False
        elif y == 95.0:
            bottom = True
            top = False
        elif y == -95.0:
            top = True
            bottom = False

        if key == GLUT_KEY_PAGE_DOWN:
            sm -= 1
            if x == 95.0:
                right = True
                left = False
            elif x == -95.0:
                left = True
                right = False
            elif y == 95.0:
                bottom = False
                top = True
            elif y == -95.0:
                top = False
                bottom = True

        if sm <= 0:
            sm = 0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE )
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Translation: ")
    glutDisplayFunc(square)
    glutIdleFunc(square)
    glutTimerFunc(0,timer,0)
    glutSpecialFunc(control)
    init()
    glutMainLoop()

main()
