from __future__ import division
from visual import *
import numpy as np

def Cod_QR(x,y,z,frameBase):
    QR = cylinder(frame=frameBase,pos=(x,y,z),radius=12,length=5,axis=(0,1,0),color=color.red)
    return QR

def Base_Carga(frameBase_Carga):
    QR = cylinder(frame=frameBase_Carga,radius=12,length=5,axis=(0,1,0),color=color.blue)
    return QR

def Obtener_Pos_XZ(a,b,p):
    aX = [] ; aZ = []; aXZ = [] ; aT = []
    aX1 = np.linspace(-a,b,p) ; aZ1 = np.linspace(-a,b,p)
    for e in aX1: aX.append(int(e))
    for e in aZ1: aZ.append(int(e))
    for i in range(len(aZ)):
        for j in range(len(aX)):
            aT.append((aX[j],aZ[i]))
        aXZ.append(aT)
        aT = []
    return aXZ

def Robot(x,y,z):
    MyRobot = frame(pos=(x,y,z))
    Base = box(frame=MyRobot,size=(45,15,45),color=color.blue)
    Led_2 = box(frame=MyRobot,size=(30,10,50),color=color.yellow)
    Sensor = cylinder(frame=MyRobot,radius=15,length=10,axis=(0,1,0),color=color.red)
    return MyRobot

Win = display(title='AGV Simulation',x=50,y=0,width=1900,height=600,center=(0,0,0))

frameBase = frame(pos=(0,0,0))
for e in range(-660,880,220):
    frameBase_Carga = frame(pos=(1320,0,e))
    #Robot(frameBase_Carga.pos.x,10,frameBase_Carga.pos.z)
    Base_Carga(frameBase_Carga)

Base = box(frame=frameBase,size=(2800,3,2800),color=color.white)
aMapa = Obtener_Pos_XZ(1100,1100,11)
for i in range(len(aMapa)):
    for j in range(len(aMapa[i])):
        Cod_QR(aMapa[i][j][0],0,aMapa[i][j][1],frameBase)



#print aXZ[0]
#Rob_1 = Robot(650,10,500)
#Rob_2 = Robot(650,10,400)

'''
while 1:
    rate(100)
    robot.rotate(angle=radians(0.1),axis=(0,1,0))
'''
