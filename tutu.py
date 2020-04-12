import pygame,random
from pygame.locals import *
from libyuang import *
 
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
        if self.order1 ==self.number1-1:
            self.order1=-1
            self.hide=1
        self.order1+=1
        self.axis1 = self.axis[self.order1]
        self.angle1 = self.angle[self.order1]
        self.rotate=pygame.transform.rotate(self.image,self.angle1)
        self.curx=self.xy[self.order1][0]+self.center1[0]
        self.cury=self.xy[self.order1][1]+self.center1[1]
        

 
pygame.init()
screen = pygame.display.set_mode((960,480),0,(32))
sui= screen.get_rect()
image2=pygame.image.load("me1.jpg")
image2=pygame.transform.scale(image2,(sui.w,sui.h))
balls = []
img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,128,78,64],[0,192,78,64]]
img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
#axis1=angle1=axis2=angle2=[]
img5=[[0,0,107,122],[0,122,107,122],[0,244,107,122],[0,366,107,122]]
img6=[[0,0,105,79],[0,79,105,79],[0,158,105,79],[0,237,105,79],[0,316,105,79],[0,395,105,79],[0,474,105,79],[0,553,105,79]]
img7=[[0,0,92,151],[0,151,92,151],[0,302,92,151],[0,453,92,151],[0,604,92,151],[0,755,92,151]]

def beisaier():
    #±´Èû¶ûÇúÏß
    #xs = [0,20,50,100,150,180,200,150,100,30,0,-50]
    #ys = [0,80,100,100,150,160,250,300,400,500,700,800]
    xs=[]
    ys=[]
    y=random.randint(0,sui.h)
    xs.append(0)
    ys.append(y)
    for i in range(2):
        x=random.randint(0,sui.w)
        y=random.randint(0,sui.h)
        xs.append(x)
        ys.append(y)
    xs.append(sui.w)
    ys.append(y)
    num = len(xs)*15
    b_xs = []
    b_ys = []
    bezier_curve(xs,ys,num,b_xs,b_ys)
    axis88=[[b_xs[i],b_ys[i]] for i in range(len(b_xs))]
    angle88,xy88=jiaodu(axis88)
    #print(angle88)
    balls.append(MoveBall("fish2.png",img1,axis88,angle88,xy88))
    
    x=random.randint(18,33)
    for j in range(6,x,6):
        t=j
        axis7=[axis88[ic] for ic in range(t,len(axis88),1)]
        #for i in range(t)[::1]:
            #axis7.append(axis88[i])
        angle7,xy7=jiaodu(axis7)
        #print(angle7)
        balls.append(MoveBall("fish2.png",img1,axis7,angle7,xy7))
#±´Èû¶ûÇúÏß
def yu2(image,img5,suiw,suih):
    axis88,angle88,xy88=beisaier2(suiw,suih)
    balls.append(MoveBall(image,img5,axis88,angle88,xy88))
    x=random.randint(18,33)
    for j in range(6,x,6):
        axis7=[axis88[ic] for ic in range(j,len(axis88),1)]
        angle7,xy7=jiaodu(axis7)
        balls.append(MoveBall(image,img5,axis7,angle7,xy7))
        

for i in range(1):
          yu2("fish5.png",img5,sui.w,sui.h)
          yu2("fish6.png",img6,sui.w,sui.h)
          yu2("fish7.png",img7,sui.w,sui.h)
          beisaier()
          beisaier()
myfont = pygame.font.SysFont("DejaVuSans", 64)


sco=0
label=0

while True:
    if pygame.event.poll().type == QUIT: break
    
 
    #screen.fill((0,0,0,))
    #current_time = pygame.time.get_ticks()
    
            

    screen.blit(image2,[0,0])
    if not len(balls):
        for i in range(1):
          yu2("fish5.png",img5,sui.w,sui.h)
          yu2("fish6.png",img6,sui.w,sui.h)
          yu2("fish7.png",img7,sui.w,sui.h)
          beisaier()
          beisaier()
        
    for b in balls:
        b.update()
        if b.hide:balls.remove(b)
        else:screen.blit(b.rotate,b.axis1)
        #pygame.draw.aalines(screen,[0,255,0],False,b.axis)
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
    pygame.time.delay(100)
    

            
