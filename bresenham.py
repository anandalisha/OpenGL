from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 100, 0, 100)


def plotLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dy > dx:
        p = (2 * dy) - dx  # decision parameter

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 1.0)
        glPointSize(5.0)
        glBegin(GL_POINTS)

        x = x1
        y = y1

        while (x <= x2):

            glVertex2f(x, y)

            if (p >= 0):
                y = y + 1
                p = p + 2 * (dy - dx)

            else:
                p = p + 2 * dy

            x = x + 1

        glEnd()
        glFlush()

    elif dx > dy:
        p = (2 * dx) - dy  # decision parameter

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 0.0)
        glPointSize(6.0)
        glBegin(GL_POINTS)

        x = x1
        y = y1

        while (y <= y2):

            glVertex2f(x, y)

            if (p >= 0):
                x = x + 1
                p = p + 2 * (dx - dy)

            else:
                p = p + 2 * dx

            y = y + 1

        glEnd()
        glFlush()


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Plot Line using Bresenham Algorithm")
    glutDisplayFunc(lambda: plotLine(x1, y1, x2, y2))
    glutIdleFunc(lambda: plotLine(x1, y1, x2, y2))
    init()
    glutMainLoop()


main()
