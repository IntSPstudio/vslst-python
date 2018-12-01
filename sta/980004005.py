#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
# ID: 980004005
# Twitter: @IntSPstudio
#|==============================================================|#

#SYSTEM
import os
import sys
#import time
import turtle
import math

#ALG
def calcCircleRl(rlRadius):
	#2PIR
	return 2*pi*rlRadius
#CONTENT SCREEN
contentscreen = turtle.Screen()
contentscreen.bgcolor("black")
#TURTLE
julle = turtle.Turtle()
julle.color("white")
julle.speed(5)
#INPUT
scriptFle = sys.argv[0]
scriptCircleRadius = sys.argv[1]
#BASIC VRB
#systemContinuity =1
pi = math.pi
inputCircleRadius = int(scriptCircleRadius)
inputCircleRl = calcCircleRl(inputCircleRadius)
inputSquareSide = inputCircleRl /4
#CLEAR SCREEN
os.system("cls")
#PRINT DATA
print("Radius:", inputCircleRadius)
print("Rl:", inputCircleRl)
print("Square:", inputSquareSide)
#ACTION
#Start position
julle.penup()
julle.right(90)
julle.forward(inputCircleRadius)
julle.left(90)
julle.pendown()
#Circle
julle.circle(inputCircleRadius)
#Next position
julle.penup()
julle.left(90)
julle.forward(inputCircleRadius)
julle.forward(inputSquareSide /2)
julle.right(90)
julle.forward(inputSquareSide /2)
julle.right(90)
julle.pendown()
#Square
julle.forward(inputSquareSide)
julle.right(90)
julle.forward(inputSquareSide)
julle.right(90)
julle.forward(inputSquareSide)
julle.right(90)
julle.forward(inputSquareSide)
#Next position
julle.penup()
julle.right(90)
julle.forward(inputSquareSide /2)
julle.right(90)
julle.forward(inputSquareSide /2)
julle.right(45)
julle.forward(inputCircleRl /4)
julle.right(180)
julle.pendown()
#Line
julle.forward(inputCircleRl /2)
#Next position
julle.penup()
julle.right(180)
julle.forward(inputCircleRl /4)
julle.right(90)
julle.forward(inputCircleRl /4)
julle.right(180)
julle.pendown()
#Line
julle.forward(inputCircleRl /2)
#Wait
contentscreen.mainloop()
os.system("cls")