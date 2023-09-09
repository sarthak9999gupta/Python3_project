#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:12:30 2023

@author: sarthakgupta
"""

import turtle 
import os

wn=turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)
wn.setup(width=900,height=1200)
wn.title("pong By Sarthak")

score_a=0
score_b=0

paddle_a=turtle.Turtle()
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=6,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400,0)

paddle_b=turtle.Turtle()
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=6,stretch_len=1)
paddle_b.penup()
paddle_b.goto(+400,0)

ball=turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

pen=turtle.Turtle()
pen.color("white")
pen.shape('square')
pen.penup()
pen.speed(0)
pen.goto(0,350)
pen.hideturtle()
pen.write("Player A: 0  Player B: 0", align='center', font=('courier',24,'normal'))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    
    if ball.ycor()>390:
        ball.sety(390)
        ball.dy *=-1
        os.system("afplay s.mp3&")
    elif ball.ycor()<-390:
        ball.sety(-390)
        ball.dy *=-1
        os.system("afplay s.mp3&")

    if ball.xcor() > 400:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -400:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    
    if (ball.xcor()<390 and ball.ycor()<paddle_b.ycor() + 60 and ball.ycor()>paddle_b.ycor() - 60):
        ball.dx *=-1
        os.system("afplay s.mp3&")
        
    elif (ball.xcor()>-390 and ball.ycor()<paddle_b.ycor() + 60 and ball.ycor()>paddle_b.ycor() - 60):
        ball.dx *=-1
        os.system("afplay s.mp3&")
    
        
        
        
        
        
        
        
