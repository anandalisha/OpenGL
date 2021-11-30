from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def square():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.6, 0.4)
    glVertex2f(0.0,50.0)
    glColor3f(0.9, 0.2, 0.3)
    glVertex2f(50.0,0.0)
    glColor3f(0.7, 1.0, 2.0)
    glVertex2f(50.0,50.0)
    glColor3f(1.5, 0.6, 0.5)
    glVertex2f(0.0,0.0)
    glColor3f(1.5, 0.6, 1.5)
    glVertex2f(25.0, 75.0)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Square")
    glutDisplayFunc(square)
    init()
    glutMainLoop()

main()
