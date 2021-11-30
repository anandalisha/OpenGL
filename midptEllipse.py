from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100, 100, -100, 100)


def plotPoint(x, y):
    glColor3f(0.0, 1.0, 0.5)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    glFlush()


def midPtEllipse(xc, yc, rx, ry):
    x = 0
    y = ry
    dx = 2 * math.pow(ry, 2) * x
    dy = 2 * math.pow(rx, 2) * y

    p1 = math.pow(ry, 2) - (math.pow(rx, 2) * ry) + 0.25 * math.pow(rx, 2)
    p2 = math.pow(ry, 2) * math.pow((x + 0.5), 2) + math.pow(rx, 2) * math.pow((y - 1), 2) - math.pow(ry, 2) * math.pow(rx, 2)

    plotPoint(x + xc, y + yc)
    while (dx < dy):
        if (p1 < 0):
            p1 = p1 + dx + math.pow(ry, 2)
        else:
            y = y - 1
            dy = dy - math.pow(rx, 2)
            p1 = p1 + dx - dy + math.pow(ry, 2)
        x += 1
        dx = dx + 2 * ry * ry
        plotPoint(x + xc, y + yc)
        plotPoint(-x + xc, y + yc)
        plotPoint(x + xc, -y + yc)
        plotPoint(-x + xc, -y + yc)

    while (dx >= dy and y >= 0):

        if (p2 > 0):
            p2 = p2 - dy + math.pow(rx, 2)
        else:
            x = x + 1
            dx = dx + math.pow(ry, 2)
            p2 = p1 + dx - dy + math.pow(rx, 2)
        y -= 1
        dy = dy - 2 * ry * ry
        plotPoint(x + xc, y + yc)
        plotPoint(-x + xc, y + yc)
        plotPoint(x + xc, -y + yc)
        plotPoint(-x + xc, -y + yc)


def main():
    xc = int(input("Enter xc: "))
    yc = int(input("Enter yc: "))
    rx = int(input("Enter rx: "))
    ry = int(input("Enter ry: "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Plot ellipse using mid point ellipse Algorithm")
    glutDisplayFunc(lambda: midPtEllipse(xc, yc, rx, ry))
    glutIdleFunc(lambda: midPtEllipse(xc, yc, rx, ry))
    init()
    glutMainLoop()


main()
