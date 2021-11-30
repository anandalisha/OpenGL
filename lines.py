from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def hLine(xmin,xmax,y):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    x = xmin
    while(x <= xmax):
        glVertex2f(x,y)
        x = x + 0.05
    glEnd()
    glFlush()

def vLine(ymin,ymax,x):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    y = ymin
    while(y <= ymax):
        glVertex2f(x,y)
        y = y + 0.05
    glEnd()
    glFlush()

def diagonalLine(x,y):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    while(x <= y):
        glVertex2f(x,x)
        x = x + 0.05
    glEnd()
    glFlush()



def main():
    choice = input("Enter Choice: ")
    if(int(choice) == 1):
        xmin = float(input("Enter x start range: "))
        xmax = float(input("Enter x end range: "))
        y = float(input("Enter Y offset: "))
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Plot Horizontal Line")
        glutDisplayFunc(lambda: hLine(xmin,xmax,y))
        glutIdleFunc(lambda: hLine(xmin,xmax,y))
        init()
        glutMainLoop()
    elif (int(choice) == 2):
        ymin = float(input("Enter y start range: "))
        ymax = float(input("Enter y end range: "))
        x = float(input("Enter x offset: "))
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Plot Vertical Line")
        glutDisplayFunc(lambda: vLine(ymin,ymax,x))
        glutIdleFunc(lambda: vLine(ymin,ymax,x))
        init()
        glutMainLoop()
    elif (int(choice) == 3):
        x = float(input("Enter start co-ordinate(x,x) as x: "))
        y = float(input("Enter end co-ordinate(y,y) as y: "))
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Plot diagonal Line")
        glutDisplayFunc(lambda: diagonalLine(x,y))
        glutIdleFunc(lambda: diagonalLine(x,y))
        init()
        glutMainLoop()
    else:
        print("Invalid choice");



main()
