from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 100, 0, 100)


def plotPoint(x, y):
    glColor3f(0.0, 1.0, 0.5)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    glFlush()


def midPtCircle(xc, yc, r):
    x = r
    y = 0
    plotPoint(x + xc, y + yc)
    if r > 0:
        plotPoint(x + xc, -y + yc)
        plotPoint(y + xc, x + yc)
        plotPoint(y + xc, x + yc)
        plotPoint(-y + xc, x + yc)

    P = 1 - r

    while x > y:

        y = y + 1

        if P <= 0:
            P = P + 2 * y + 1

        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if (x < y):
            break

        plotPoint(x + xc, y + yc)
        plotPoint(-x + xc, y + yc)
        plotPoint(x + xc, -y + yc)
        plotPoint(-x + xc, -y + yc)

        if x != y:
            plotPoint(y + xc, x + yc)
            plotPoint(-y + xc, x + yc)
            plotPoint(y + xc, -x + yc)
            plotPoint(-y + xc, -x + yc)


def main():
    x = int(input("\nEnter center:\n\tx: "))
    y = int(input("\ty: "))
    r = int(input("Radius: "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Plot Circle using Midpoint Circle Drawing Algorithm")
    glutDisplayFunc(lambda: midPtCircle(x, y, r))
    glutIdleFunc(lambda: midPtCircle(x, y, r))
    init()
    glutMainLoop()


main()
