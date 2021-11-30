from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

from math import pi, tan, radians, sin, cos

import sys

WINDOW_SIZE = 500

X = Y = 0
SPEED = 1
OFFSET = 0
TO_RIGHT = True


def init():
    glClearColor(0.0, 0.0, 0.0, 1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def get_input():
    global SPEED, ANGLE, RADIUS, X1, Y1, X2, Y2, TO_RIGHT
    ANGLE = float(input("Enter the inclination of the line: "))
    RADIUS = int(input("Enter the radius of the ball: "))
    X1, Y1 = -WINDOW_SIZE, -WINDOW_SIZE * tan(radians(ANGLE))
    X2, Y2 = WINDOW_SIZE, WINDOW_SIZE * tan(radians(ANGLE))
    if ANGLE >= 0:
        TO_RIGHT = False
    else:
        TO_RIGHT = True


def create_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(X1, Y1)
    glVertex2f(X2, Y2)
    glEnd()


def update(value):
    global X, Y, SPEED, TO_RIGHT, OFFSET
    if TO_RIGHT:
        X += SPEED * cos(radians(ANGLE))
        Y += SPEED * sin(radians(ANGLE))
        OFFSET -= 0.01 * SPEED
    else:
        X -= SPEED * cos(radians(ANGLE))
        Y -= SPEED * sin(radians(ANGLE))
        OFFSET += 0.01 * SPEED
    if X > WINDOW_SIZE - RADIUS:
        TO_RIGHT = False
    elif X < -WINDOW_SIZE + RADIUS:
        TO_RIGHT = True
    elif Y > WINDOW_SIZE - RADIUS:
        TO_RIGHT = False
    elif Y < -WINDOW_SIZE + RADIUS:
        TO_RIGHT = True
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), update, 0)


def draw_circle(x, y):
    global OFFSET
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        glColor3f(1, 0, 1)
        glVertex2f(RADIUS * cos(OFFSET + pi * i / 180) + x,
                   RADIUS * sin(OFFSET + pi * i / 180) + y)
    glEnd()


def display():
    global X, Y
    create_line()
    draw_circle(X - RADIUS * sin(radians(ANGLE)),
                Y + RADIUS * cos(radians(ANGLE)))
    glutSwapBuffers()


def controls(key, x, y):
    global TO_RIGHT
    global SPEED
    if key == b"d":
        TO_RIGHT = True
    elif key == b"a":
        TO_RIGHT = False
    elif key == b"w":
        SPEED += 1
    elif key == b"s":
        SPEED -= 1
        if SPEED < 0:
            SPEED = 0


def main():
    get_input()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Ball Rolling Program")
    glutDisplayFunc(display)
    glutKeyboardFunc(controls)
    glutTimerFunc(0, update, 0)
    glutIdleFunc(display)
    init()
    glutMainLoop()


#if _name_ == "_main_":
main()
