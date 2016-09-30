#|==============================================================|#
# Made by IntSPstudio
# Project Visual Street
#
# Twitter: @IntSPstudio
#|==============================================================|#

#SYSTEM
import os
import sys
#import time
import turtle
import math

#ALG
#Ympyrän kehän koko
def calcCircleRl(rlRadius):
	#2PIR
	output = 2*pi*rlRadius
	return output
#Laskee piiraan kehän koon
def calcCircleSliceRl(rlAngle,rlRadius):
	output = rlAngle/360*pi*rlRadius*2
	return output
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
scriptCircleSliceAngle = sys.argv[2]
#BASIC VRB
#systemContinuity =1
pi = math.pi
inputCircleRadius = int(scriptCircleRadius)
inputCircleSliceAngle = int(scriptCircleSliceAngle)
inputCircleRl = calcCircleRl(inputCircleRadius)
inputCircleSliceRl = calcCircleSliceRl(inputCircleSliceAngle,inputCircleRadius)
#CLEAR SCREEN
os.system("cls")
#PRINT DATA
print("   Radius:", inputCircleRadius)
print("    Slice:", scriptCircleSliceAngle)
print("Circle Rl:", inputCircleRl)
print(" Slice Rl:", inputCircleSliceRl)
print("     %Rld:", inputCircleSliceRl / inputCircleRl *100)
#ACTION
#Start position
julle.penup()
julle.forward(inputCircleRadius)
julle.left(90)
julle.pendown()
#Circle
julle.circle(inputCircleRadius)
#Slice
julle.pendown()
julle.left(90)
julle.forward(inputCircleRadius)
julle.right(180 - inputCircleSliceAngle)
julle.forward(inputCircleRadius)
julle.right(180)
julle.forward(inputCircleRadius)
#Wait
contentscreen.mainloop()
os.system("cls")

#
#		................................
#		||||||||||||||||||||||||||||||||
#		......||................||......
#		......||................||......
#		......||................||......
#		......||................||......
#		......||.....Tatu.T.....||......
#		......||................||......
#		......||.......##.......||......
#		................................
#
# Sä elät tätä päivää jos nyt jo luot huomista