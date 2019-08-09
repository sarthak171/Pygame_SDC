import math
import pygame as pg
from pygame.locals import *
import random as rand

pg.init()

clock = pg.time.Clock()

gameDisplay = pg.display.set_mode((1280,720),pg.RESIZABLE)
gameDisplay.fill((0,0,0))

end = False

class deathBall:
	def __init__(self):
		self.x = rand.randint(0,1280)
		self.y = rand.randint(0,720)
		self.size = rand.randint(10,100)
		if(rand.random()>.5):
			self.x_speed = -rand.randint(2,5)
		else:
			self.x_speed = rand.randint(2,5)
		if(rand.random()>.5):
			self.y_speed = -rand.randint(2,5)
		else:
			self.y_speed = rand.randint(2,5)
		self.color = (rand.randint(100,200),rand.randint(100,200),rand.randint(100,200))
	def move(self):
		#self.x=self.x+int(self.speed*math.cos((math.radians(self.angle))))
		#self.y=self.y+int(self.speed*math.sin((math.radians(self.angle))))
		self.x+=self.x_speed
		self.y+=self.y_speed
	def bounce(self):
		if(self.x<=0 or self.x >=1280):
			self.x_speed = -self.x_speed
		if(self.y<=0 or self.y>=720):
			self.y_speed = -self.y_speed

class Player:
	def __init__(self):
		self.x = int(1280/2)
		self.y= int(760/2)
		self.size = 20
		self.color = (255,255,255)
	def move(self,keys):
		if keys[K_w]:
			self.y-=3
		if(keys[K_s]):
			self.y+=3     
		if(keys[K_d]):
			self.x+=3       
		if(keys[K_a]):
			self.x-=3
		if(self.x<=0 or self.x >=1280):
			self.x = 0
		if(self.y<=0 or self.y>=720):
			self.y = 0
	def checkCol(self,dBall):
		if(math.sqrt((dBall.x-self.x)**2+(dBall.y-self.y)**2)<=dBall.size+self.size):
			return True
		return False

me = Player()

deathBalls = []
for i in range(0,15):
	deathBalls.append(deathBall())
while not end:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True
    gameDisplay.fill((0,0,0))
    keys = pg.key.get_pressed()
    me.move(keys)
    for dBall in deathBalls:
    	dBall.move()
    	dBall.bounce()
    	if(me.checkCol(dBall)):
    		me = Player()
    		deathBalls = []
    		for i in range(0,15):
    			deathBalls.append(deathBall())
    		continue
    	pg.draw.circle(gameDisplay,dBall.color,(dBall.x,dBall.y),dBall.size)
    pg.draw.circle(gameDisplay,me.color,(me.x,me.y),me.size)
    
    pg.display.update()

    clock.tick(60)
pg.quit()
quit()