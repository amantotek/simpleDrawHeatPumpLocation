#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Run like: $ python3 heatPumpLoc.py
#x horizontal left to right, y vertical bot to top
#0,0 bottom fence in 1pp garden
#Nb Neighbour. AsPt Assessment Position. All dimensions metres
import math 
import turtle
from datetime import date
t = turtle.Turtle()

SCL=50 #Scaling to multiply metres by to give screen pixels
XSHIFTREF=2 #Shift reference 0,0 so many metres left
pi=3.14159

xNbAlleyway=0.89
xNbEdgeToUpWindow=1.12
yNbGroundUp=0.5
x1ppAlleyway=1.06

#Nb Assessment window
xAsPtWindow=1.9
yAsPtWindow=1.08
yAsPtWindowRefToBottom=3.85
xAsPtCentre = -(xNbAlleyway+xNbEdgeToUpWindow+(xAsPtWindow/2))
yAsPtCentre = yNbGroundUp+yAsPtWindowRefToBottom+(yAsPtWindow/2)
xAsPtWindTopLeft = -(xNbAlleyway+xNbEdgeToUpWindow+xAsPtWindow)
yAsPtWindTopLeft = yNbGroundUp+yAsPtWindowRefToBottom+yAsPtWindow
sgOpTxt = "KEY:\n(x along ->, y up ^)\nReference is fence bottom (0,0).\nAll in metres.\n\nObject ,Top Left(X,Y), Size(x,y)\n" #Note2

yFenceHeight=2

#Heat Pump
xHTP=1.38
yHTP=0.87
yBaseHP=0.2
xFromWestWall=5.3 #This needs to be minimised as long as Note1 is >= 10m

yDoorHeight=2.22
xDoorWidth=0.83
xKitcWind=2.45
yKitcWind=1.12
yHeightKitWindBot=1.0
xBackdoorToWindow=0.6
yBench=0.9
xBench=1.7

def drArrowedLn(x1,y1,x2,y2,bAddLength=False):
  iRetn=drLn(x1,y1,x2,y2,bAddLength)
  addArrowHeds(x1,y1,x2,y2)
  return iRetn

def drLn(x1,y1,x2,y2,bAddLength=False):
  #Return length of line as string if bAddLength is True
  xs1=(x1-XSHIFTREF)*SCL
  ys1=y1*SCL
  xs2=(x2-XSHIFTREF)*SCL
  ys2=y2*SCL
  t.up()
  t.goto(xs1,ys1)
  t.down()
  t.goto(xs2,ys2)
  t.up()
  iDist=0
  if bAddLength == True:
    pp = [x1,y1]
    qq = [x2,y2]
    iDist = math.dist(pp, qq) # Calculate Euclidean distance
    sDist = "{}m".format(round(iDist,2))
    print(sDist)
    xMidPoint = (xs1 + xs2)/2
    yMidPoint = (ys1 + ys2)/2
    t.goto(xMidPoint,yMidPoint)
    t.hideturtle()
    t.penup()
    t.write(sDist, font=("Verdana", 10, "normal"))
    #t.write(message,move=False, font=(sDist,30,'bold'),align='left')
    t.up()
  return iDist

def addArrowHeds(x1,y1,x2,y2):
  dd=0.3 #Arrow length
  #head 1
  aga= math.atan((y1-y2)/(x2-x1)) #returns between  -PI/2 and PI/2 radians.
  #45degs = pi/4 radians
  agb = (pi/4)-aga
  y31=dd*math.sin(agb) #y31=y3-y1
  x31=dd*math.cos(agb) #x31=x3-x1
  y3=y31+y1
  x3=x31+x1
  #head 2
  anh=(pi/2)-aga #90-aga
  ang=anh - (pi/4) #anh-45
  x41=dd*math.sin(ang) #x41=x4-x1
  y14=dd*math.cos(ang) #y14=y1-y4
  x4=x41+x1
  y4 = y1-y14 
  y62=y14 #y62=y6-y2
  x26=x41 #x26=x2-x6
  y6=y62+y2
  x6=x2-x26
  x25=x31 #x25=x2-x5
  y25=y31 #y25=y2-y5
  x5=x2-x25
  y5=y2-y25
  drLn(x1,y1,x3,y3)
  drLn(x1,y1,x4,y4)
  drLn(x2,y2,x5,y5)
  drLn(x2,y2,x6,y6)
  
def recct(xTopleft,yTopLeft,xLn,yLn,sDesc=""):
  #xLn is horizontal rectangle length and yLn vertical length
  global sgOpTxt
  drLn(xTopleft,yTopLeft,xTopleft+xLn,yTopLeft) #To East
  drLn(xTopleft+xLn,yTopLeft,xTopleft+xLn,yTopLeft-yLn) #To South
  drLn(xTopleft+xLn,yTopLeft-yLn,xTopleft,yTopLeft-yLn) #To West
  drLn(xTopleft,yTopLeft-yLn,xTopleft,yTopLeft) #To North
  if sDesc != "":
    sgOpTxt += "{} ({},{}),({},{})\n".format(sDesc,round(xTopleft,2),round(yTopLeft,2),round(xLn,2),round(yLn,2)) #See Note2 above for header
    #Write in rectangle a two character descriptor
    drLn(xTopleft,yTopLeft-0.4,xTopleft,yTopLeft-0.4)
    t.write(sDesc[:2], font=("Verdana", 10, "normal"))

drLn(0,0,0,yFenceHeight, True) #Fence

yHseWalls=6 #metres to above assessment window
drLn(-xNbAlleyway,yNbGroundUp,-xNbAlleyway,yHseWalls+yNbGroundUp) #Nb house side east facing UP
drLn(x1ppAlleyway,0,x1ppAlleyway,yHseWalls) #1pp house side west facing UP
#House bases
drLn(-xNbAlleyway,yNbGroundUp,-xNbAlleyway-6,yNbGroundUp) #
drLn(x1ppAlleyway,0,x1ppAlleyway+10,0) #1pp house side west facing UP

recct(xAsPtWindTopLeft,yAsPtWindTopLeft,xAsPtWindow,yAsPtWindow,"AW Nb Assessment Window")
#Show Assessment Position as cross
CRSZ=0.02 #Half Cross span in metres
drLn(xAsPtCentre-CRSZ,yAsPtCentre,xAsPtCentre+CRSZ,yAsPtCentre)
drLn(xAsPtCentre,yAsPtCentre-CRSZ,xAsPtCentre,yAsPtCentre+CRSZ)

xWestWallToBackDoor=2.08
recct(xWestWallToBackDoor,yDoorHeight,xDoorWidth,yDoorHeight,"BD Back Door")

recct(xWestWallToBackDoor+xDoorWidth+xBackdoorToWindow,yHeightKitWindBot+yKitcWind,xKitcWind,yKitcWind,"KW Kitchen Window")

#Bench by open backdoor
recct(xWestWallToBackDoor+xDoorWidth+xBackdoorToWindow,yBench,xBench,yBench,"GB Garden Bench")

#Heat Pump
xHPTl=x1ppAlleyway+xFromWestWall #Top Left HP along
yHPTl=yBaseHP+yHTP #Top Left HP up
recct(xHPTl,yHPTl,xHTP,yHTP,"HP Daikin Altherma HC Monobloc Heat Pump")

#MCS Horizontal Distance/Line from Assessment position to closest edge of Heat Pump Note1
drArrowedLn(xAsPtCentre,yAsPtCentre,xHPTl,yHPTl,True)

#Distance/Line Nb Assessment Window furtherest edge to fence
drArrowedLn(xAsPtWindTopLeft,-1,0,-1,True)

#Distance/Line from West wall 1pp to mid HP for external pipework
iUmExternal = drArrowedLn(x1ppAlleyway,-1,xHPTl+(xHTP/2),-1,True) #Take pipes to midway along HP
#addArrowHeds(x1ppAlleyway,-1,xHPTl+(xHTP/2),-1)
iUmInternal = 2.3 #See heatPump.seml/html Measured from back door into utility room almost far side

iUmbilLen = iUmExternal+iUmInternal
sUmbilLen = "Umbilical length: Internal {}m, Total {}m".format(iUmInternal,round(iUmbilLen,2))
drLn(x1ppAlleyway,-2,x1ppAlleyway,-2) #Just to reposition turtle below the Horizontal Distance-line
t.write(sUmbilLen, font=("Verdana", 10, "normal"))

#Title at top right
today = date.today()
d4 = today.strftime("%d-%b-%Y")
drLn(x1ppAlleyway+0.1,yAsPtWindTopLeft,x1ppAlleyway+0.1,yAsPtWindTopLeft) #Just to reposition turtle below the Horizontal Distance-line
sHdr="{}\n10 Downing St London SW1A 2AB\n".format(d4)
t.write(sHdr, font=("Verdana", 10, "normal"))

drLn(0,0.01,0,0) #Park at bottom of fence
turtle.done()
t.screen.mainloop()
print(sgOpTxt)
