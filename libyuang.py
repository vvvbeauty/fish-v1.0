import numpy as np
import math,random
import pygame,random
from pygame.locals import *
BusX=70
BusY=00


class Ball(pygame.sprite.Sprite):
    def __init__(self, file1,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.order=0
        self.images1 = pygame.image.load(file1)
        self.images=[self.images1.subsurface(i) for i in initial_position]
        self.image=self.images[self.order]
        self.rect=self.image.get_rect()
        self.imagex=self.rect.w
        self.imagey=self.rect.h
        self.center1=self.rect.center
        self.number=len(initial_position)
        #self.rect = self.image.fill(color, None, BLEND_ADD)
        #self.rect.topleft = initial_position

class MoveBall(Ball):
    def __init__(self, file1, initial_position, axis, angle,xy):
        super(MoveBall, self).__init__(file1, initial_position)
        self.count=0
        self.hide=0
        self.order1=0
        self.axis=axis
        self.angle=angle
        self.axis1 = self.axis[self.order1]
        self.angle1 = self.angle[self.order1]
        self.number1=len(angle)
        self.rotate=pygame.transform.rotate(self.image,self.angle1)
        self.xy=xy
        self.curx=self.xy[self.order1][0]+self.center1[0]
        self.cury=self.xy[self.order1][1]+self.center1[1]
        
        
 
    def update(self):
        self.count+=1
        if self.order >=self.number-1:
            self.order=-1
            
        self.order+=1
        self.image=self.images[self.order]
        #if self.order1 >=self.number1-1:
            #self.order1=-1
            #self.hide=1
        #else:self.order1+=1
        #self.axis1 = self.axis[self.order1]
        #self.angle1 = self.angle[self.order1]
        #self.rotate=pygame.transform.rotate(self.image,self.angle1)
        #self.curx=self.xy[self.order1][0]+self.center1[0]
        #self.cury=self.xy[self.order1][1]+self.center1[1]
        if self.order1 >=self.number1-1 :
            self.order1=-1
            self.hide=1
        else:
            self.order1+=1
            self.axis1 = self.axis[self.order1]
            self.angle1 = self.angle[self.order1]
            self.rotate=pygame.transform.rotate(self.image,self.angle1)
            self.curx=self.xy[self.order1][0]+self.center1[0]
            self.cury=self.xy[self.order1][1]+self.center1[1] 


 
def yuang(banjinX,banjinY,currX,currY,Ty=360,Xstep=5,er=2,Xv=0,Yv=0):
	
  plotPoints = []
  angle=[]
  #Ty=360
  for i in range(0,Ty,Xstep):
      if not Yv:
          y = int(math.sin(i / Ty *er* math.pi) * banjinY+currY )
      if Yv: y=i
      if not Xv:x=int(math.cos(i / Ty *er* math.pi) * banjinX+currX )
      if Xv: x=i
      plotPoints.append([x, y])
  angle=jiaodu(plotPoints)
   
  return plotPoints,angle
   
def jiaodu(plotPoints): 	
  angle=[]
  xy=[]
  for i in range(len(plotPoints)-1):
  	x=plotPoints[i+1][0]-plotPoints[i][0]
  	y=plotPoints[i+1][1]-plotPoints[i][1]
  	xy.append([x,y])
  	z=math.atan2(y,x)
  	j=(-math.degrees(z))%360
  	j+=0
  	angle.append(j)
  	#print(i,x,y,j)
  
  i=len(plotPoints)-1
  x=plotPoints[i][0]-plotPoints[i-1][0]
  y=plotPoints[i][1]-plotPoints[i-1][1]
  xy.append([x,y])
  z=math.atan2(y,x)
  j=(-math.degrees(z)+180)%360
  j+=0
  angle.append(j)
  #print(i,x,y,j)
  xy=realxy(plotPoints,xy)
  return angle,xy
def realxy(plot,xy):
  for i in range(len(plot)):
    plot[i][0]=plot[i][0]+xy[i][0]
    plot[i][1]=plot[i][1]+xy[i][1]
  return plot

def one_bezier_curve(a,b,t):
    return (1-t)*a + t*b

def n_bezier_curve(xs,n,k,t):
    if n == 1:
        return one_bezier_curve(xs[k],xs[k+1],t)
    else:
        return (1-t)*n_bezier_curve(xs,n-1,k,t) + t*n_bezier_curve(xs,n-1,k+1,t)
      
def bezier_curve(xs,ys,num,b_xs,b_ys):
    n = len(xs) - 1
    t_step = 1.0 / (num - 1)
    t = np.arange(0.0,1+t_step,t_step)
    for each in t:
        b_xs.append(n_bezier_curve(xs,n,0,each))
        b_ys.append(n_bezier_curve(ys,n,0,each))

def beisaier2(sui_w=960,sui_h=480,num1=2):
    #bei sai er qu xian
    #xs = [0,20,50,100,150,180,200,150,100,30,0,-50]
    #ys = [0,80,100,100,150,160,250,300,400,500,700,800]
    
    xs=[]
    ys=[]
    y=random.randint(0,sui_h)
    xs.append(0-BusX)
    ys.append(y-BusY)
    for i in range(num1):
        x=random.randint(0,sui_w)
        y=random.randint(0,sui_h)
        xs.append(x)
        ys.append(y)
    xs.append(sui_w)
    ys.append(y)
    num = len(xs)*15
    b_xs = []
    b_ys = []
    bezier_curve(xs,ys,num,b_xs,b_ys)
    axis88=[[int(b_xs[i]),int(b_ys[i])] for i in range(len(b_xs))]
    angle88,xy88=jiaodu(axis88)
    return axis88,angle88,xy88

def yu2(image,img5,suiw,suih,t=5,num1=2):
    balls=[]
    axis88,angle88,xy88=beisaier2(suiw,suih,num1)
    for i in range(t):
        balls.append(MoveBall(image,img5,axis88,angle88,xy88))
    #x=random.randint(7,25)
    #for j in range(6,x,6):
        #axis7=[axis88[ic] for ic in range(j,len(axis88),1)]
        #angle7,xy7=jiaodu(axis7)
        #balls.append(MoveBall(image,img5,axis7,angle7,xy7))
    return balls
  
 
