import numpy as np
import math,random
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

def beisaier2(sui_w=960,sui_h=480):
    #bei sai er qu xian
    #xs = [0,20,50,100,150,180,200,150,100,30,0,-50]
    #ys = [0,80,100,100,150,160,250,300,400,500,700,800]
    xs=[]
    ys=[]
    y=random.randint(0,sui_h)
    xs.append(0)
    ys.append(y)
    for i in range(2):
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
    axis88=[[b_xs[i],b_ys[i]] for i in range(len(b_xs))]
    angle88,xy88=jiaodu(axis88)
    return axis88,angle88,xy88
   
    
 
