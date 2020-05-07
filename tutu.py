import pygame,random
from pygame.locals import *
from libyuang import *
from Ffile import *

BusX=500
BusY=100

pygame.init()
screen = pygame.display.set_mode((960,480),0,(32))
sui= screen.get_rect()
image2=pygame.image.load("me1.jpg")
image2=pygame.transform.scale(image2,(sui.w,sui.h))
balls = []
temp=[]
img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,128,78,64],[0,192,78,64]]
img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
#axis1=angle1=axis2=angle2=[]
img5=[[0,0,107,122],[0,122,107,122],[0,244,107,122],[0,366,107,122]]
img6=[[0,0,105,79],[0,79,105,79],[0,158,105,79],[0,237,105,79],[0,316,105,79],[0,395,105,79],[0,474,105,79],[0,553,105,79]]
img7=[[0,0,92,151],[0,151,92,151],[0,302,92,151],[0,453,92,151],[0,604,92,151],[0,755,92,151]]
#temp.append(yu2("fish2.png",img1,sui.w,sui.h))
#temp1=yu2("fish2.png",img1,sui.w,sui.h,8)
#temp=temp1
#balls.append(temp[0])
#print(dir(balls))
#print(dir(temp[0]))


myfont = pygame.font.SysFont("DejaVuSans", 64)


sco=0
label=0



while True:
    if pygame.event.poll().type == QUIT: break
    
 
    #screen.fill((0,0,0,))
    #current_time = pygame.time.get_ticks()
    
    if not len(balls):
        max1=random.randint(4,10)
        temp=yu2("fish2.png",img1,sui.w,sui.h,max1)
        app=AddBall(balls,temp,max1,5)
    screen.blit(image2,[0,0])
    balls=app.update()
    
    dead_ball=[]
    
    for c in balls:
        c.update()
        screen.blit(c.rotate,c.axis1)
        if c.hide:dead_ball.append(c)
          
        #pygame.draw.aalines(screen,[0,255,0],False,b.axis)
   
    
    for b in dead_ball:
        balls.remove(b)
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #if event.button==1:
               
               label = myfont.render('{0}'.format(event.pos), 1, (255, 255, 255))
               for b in balls:
                   b.update()
                   x=abs(int(event.pos[0]-b.curx))
                   y=abs(int(event.pos[1]-b.cury))
                   if x<b.imagex/2 and y<b.imagey/2:
                       sco+=1
                       balls.remove(b)
                       
                   
    label1= myfont.render("score:{}".format(sco), 1, (255, 255, 255))                
    
    screen.blit(label1,(0,0))
    if label:
        screen.blit(label, (420, 0))
        
    pygame.display.update()
    pygame.time.delay(200)
   
    

            
