# -*- coding: utf-8 -*-
# @Time    : 2019/1/27
# @Author  : Clark Du
# @简介    : 
# @File    : paint.py


import turtle
import math


def main():
    ttl = turtle.Turtle()
    ttl.speed(1)
    turtle.screensize(800, 600)
    # ttl.pensize(5)
    # draw_func(ttl, f, -2, 2, 0.1)

    ttl.home()
    ttl.pendown()
    ttl.pensize(10)
    ttl.pencolor('orangered')
    arc(ttl, 200, 60)
    # ttl.circle(200, 270)
    turtle.done()


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1         # 线段条数
    step_length = arc_length / n        # 每条线段的长度
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def f(x):
    return x * x


def draw_func(ttl, fn, lower, upper, step):
    SCALE = 50
    ttl.penup()
    x = lower
    y = fn(x)
    scaledX = x * SCALE
    scaledY = y * SCALE
    ttl.goto(scaledX, scaledY)
    ttl.pendown()
    while x < upper:
        x = x + step
        y = fn(x)
        scaledX, scaledY = x * SCALE, y * SCALE
        ttl.goto(scaledX, scaledY)
    ttl.penup()


main()

