from __future__ import division
from visual import *
import numpy as np
from time import sleep

pi=3.14

def qrs(y):
    barra_1=cylinder(pos=(y,0,50),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,150),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,150),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,250),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,350),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,450),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,550),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,650),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,-50),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,-150),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,-250),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,-350),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,-450),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,-550),color=color.red,radius=10,axis=(0,1,0),length=3)
    barra_1=cylinder(pos=(y,0,-650),color=color.red,radius=10,axis=(0,1,0),length=3)

def Robot(x,y,z):
    MyRobot = frame(pos=(x,y,z))
    Base = box(frame=MyRobot,size=(45,15,45),color=color.blue)
    Led_1 = box(frame=MyRobot,size=(50,10,30),color=color.yellow)
    Led_2 = box(frame=MyRobot,size=(30,10,50),color=color.yellow)
    Sensor = cylinder(frame=MyRobot,radius=15,length=10,axis=(0,1,0),color=color.red)
    return MyRobot

def mover_treal(robot):
 
    print robot.pos()
    

def Mover_Robot_z(robot,xi,yi,zi):
    while(1):
        zi=zi+1
        if zi==650 or zi==-650:
            break
        robot.pos=(xi,yi,zi)
        sleep(0.01)

def Mover_Robot_x(robot,xi,yi,zi):
    while(1):
        xi=xi+1
        if xi==650 or xi==-650:
            break
        robot.pos=(xi,yi,zi)
        sleep(0.01)

def girar_Robot_x(robot,axis,pos):
    robot.rotate(angle=pi/4, axis=axis, origin=pos)

Win = display(title='AGV Simulation',x=50,y=0,width=1900,height=600,center=(0,0,0))
Base = box(pos=(0,0,0),size=(1600,3,1600),color=color.white)
Rob_1 = Robot(250,10,150)
Rob_2 = Robot(550,10,-50)
Rob_3 = Robot(50,10,-250)
Rob_4 = Robot(150,10,-150)
Rob_5 = Robot(-250,10,350)
Rob_6 = Robot(-150,10,250)
Rob_7 = Robot(350,10,-50)

qrs(50)
qrs(150)
qrs(250)
qrs(350)
qrs(450)
qrs(550)
qrs(650)
qrs(-50)
qrs(-150)
qrs(-250)
qrs(-350)
qrs(-450)
qrs(-550)
qrs(-650)

while 1:
    Mover_Robot_x(Rob_1,250,10,150)
    Mover_Robot_z(Rob_2,550,10,-50)
    Mover_Robot_x(Rob_3,50,10,-250)
    Mover_Robot_z(Rob_4,150,10,-150)
    Mover_Robot_x(Rob_5,-250,10,350)
    Mover_Robot_z(Rob_6,-150,10,250)
    girar_Robot_x(Rob_1,(0,1,0),(250,10,150))



