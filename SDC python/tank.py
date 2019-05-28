import math
import pygame as pg
from pygame.locals import *


tank1_x = 50
tank1_y = 50
tank1_rad = 30
tank1_ang = 0
bullets1 = []
score1 = 0

tank2_x = 1200
tank2_y = 600
tank2_rad = 30
tank2_ang = 180
bullets2 = []
score2 = 0

def shootBullet(tanknum):
    if(tanknum == 1):
        bullets1.append([tank1_x,tank1_y,tank1_ang,7*math.cos(math.radians(tank1_ang)),7*math.sin(math.radians(tank1_ang))])
    else:
        bullets2.append([tank2_x,tank2_y,tank2_ang,7*math.cos(math.radians(tank2_ang)),7*math.sin(math.radians(tank2_ang))])
def checkBorderCol(x,y):
    check = False
    if(x<=0):
        x+=20
        check = True
    elif(x+40>=1280):
        x-=20
        check = True
    elif(y<=0):
        y+=20
        check = True
    elif(y+40>=720):
        y-=20
        check = True
    return x,y,check
def updateBullets():
    for bul in bullets1:
        bul[0] += bul[3]
        bul[1] += bul[4]
        blah,blah,check = checkBorderCol(bul[0],bul[1])
        if (check):
            bullets1.remove(bul)
    for bul in bullets2:
        bul[0] += bul[3]
        bul[1] += bul[4]
        blah,blah,check = checkBorderCol(bul[0],bul[1])
        if (check):
            bullets2.remove(bul)
def colBul_Bul():
    for bul1 in bullets1:
        for bul2 in bullets2:
            if(math.sqrt((bul2[0]-bul1[0])**2+(bul2[1]-bul1[1])**2)<=10):
                bullets1.remove(bul1)
                bullets2.remove(bul2)
                return
def colBul_Tank():
    global score1o
    global score2
    for bul2 in bullets2:
        if(math.sqrt((bul2[0]-tank1_x)**2+(bul2[1]-tank1_y)**2)<=35):
            bullets2.remove(bul2)
            score2 = score2+1
            return
    for bul1 in bullets1:
        if(math.sqrt((bul1[0]-tank2_x)**2+(bul1[1]-tank2_y)**2)<=35):
            bullets1.remove(bul1)
            score1 = score1+1
            return

#tank2 
#score
pg.init()
pg.font.init()
myFont = pg.font.SysFont('Comic Sans MS',30)
#use google drive to share collision methods




gameDisplay = pg.display.set_mode((1280,720),pg.RESIZABLE)
gameDisplay.fill((255,255,255))

#tank1 = pg.draw.circle(gameDisplay,(255,0,0),(tank1_x,tank1_y),tank1_rad)
#tank2 = pg.draw.circle(gameDisplay,(0,255,0),(tank2_x,tank2_y),tank2_rad)



clock = pg.time.Clock()


end = False

while not end:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True
        #print(event)
    tank1_x,tank1_y,blah=checkBorderCol(tank1_x,tank1_y)
    tank2_x,tank2_y,blah=checkBorderCol(tank2_x,tank2_y)

    keys = pg.key.get_pressed()
    if keys[K_w]:
        tank1_y-=3
    if(keys[K_s]):
        tank1_y+=3     
    if(keys[K_d]):
        tank1_x+=3       
    if(keys[K_a]):
        tank1_x-=3
    if(keys[K_1]):
        tank1_ang-=3
    if(keys[K_2]):
        tank1_ang+=3

    if keys[K_UP]:
        tank2_y-=3
    if(keys[K_DOWN]):
        tank2_y+=3     
    if(keys[K_RIGHT]):
        tank2_x+=3       
    if(keys[K_LEFT]):
        tank2_x-=3
    if(keys[K_n]):
        tank2_ang-=3
    if(keys[K_m]):
        tank2_ang+=3
    shootBullet(1)
    shootBullet(2)

    gameDisplay.fill((255,255,255))
    updateBullets()
    colBul_Bul()
    colBul_Tank()
    for bul in bullets1:
        pg.draw.circle(gameDisplay,(255,0,0),(int(bul[0]),int(bul[1])),5)
    for bul in bullets2:
        pg.draw.circle(gameDisplay,(0,255,0),(int(bul[0]),int(bul[1])),5)

    tank1 = pg.draw.circle(gameDisplay,(255,0,0),(tank1_x,tank1_y),tank1_rad)
    tank1_aim = pg.draw.line(gameDisplay,(0,0,0),(tank1_x,tank1_y),(tank1_x+tank1_rad*math.cos(math.radians(tank1_ang)),tank1_y+tank1_rad*math.sin(math.radians(tank1_ang))),5)
    
    tank2 = pg.draw.circle(gameDisplay,(0,255,0),(tank2_x,tank2_y),tank2_rad)
    tank2_aim = pg.draw.line(gameDisplay,(0,0,0),(tank2_x,tank2_y),(tank2_x+tank2_rad*math.cos(math.radians(tank2_ang)),tank2_y+tank2_rad*math.sin(math.radians(tank2_ang))),5)
    

    textBox1 = myFont.render(str(score1),True,(255,0,0))
    textBox2 = myFont.render(str(score2),True,(0,255,0))
    gameDisplay.blit(textBox1,(0,0))
    gameDisplay.blit(textBox2,(1200,0))
    pg.display.update()
    clock.tick(60)
pg.quit()
quit()