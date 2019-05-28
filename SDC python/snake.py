import pygame as pg
from pygame.locals import *
import random as rand
import math
class food:
	x = 0
	y = 0
	def __init__(self):
		self.x = int(rand.random()*500)
		self.y = int(rand.random()*500)
	def draw(self,surface):
		pg.draw.circle(surface,(0,255,0),(self.x,self.y),10)
class player:
	x = [50,40,30,20]
	y = [50,50,50,50]
	tail = 4
	speed = 15
	def checkBorderCol(self):
		check = False
		if(self.x[0]<=0):	    
		    check = True
		elif(self.x[0]+10>=505):    
		    check = True
		elif(self.y[0]<=0):
		    check = True
		elif(self.y[0]+10>=505):
		    check = True
		return check
	def foodCol(self,x,y):
		if(math.sqrt((y-self.y[0])**2+(x-self.x[0])**2)<=20):
			self.x.append(self.x[self.tail-1])
			self.y.append(self.y[self.tail-1])
			self.tail +=1
			return True
		return False
	def checkSelfCol(self):
		for t in range(3,self.tail):
			if(math.sqrt((self.y[t]-self.y[0])**2+(self.x[t]-self.x[0])**2)<=15):
				return True
		return False
	def moveRight(self):
		self.x[0] = self.x[0] -self.speed
	def moveLeft(self):
		self.x[0] = self.x[0] + self.speed
	def moveUp(self):
		self.y[0] = self.y[0] - self.speed
	def moveDown(self):
		self.y[0] = self.y[0] +self.speed
	def updateOld(self):
		i = self.tail-1
		while i > 0:
			self.x[i] = self.x[i-1]
			self.y[i] = self.y[i-1]
			i-=1
	def draw(self,surface):
		for i in range(self.tail):
			pg.draw.circle(surface,(255,0,0),(self.x[i],self.y[i]),10)
pg.init()
gameDisplay = pg.display.set_mode((500,500),pg.RESIZABLE)
gameDisplay.fill((0,0,0))
clock = pg.time.Clock()
end = False
snake = player()
goal = food()
w = False
a = False
s = False
d = True
while not end:
	for event in pg.event.get():
	    if event.type == pg.QUIT or snake.checkBorderCol() or snake.checkSelfCol():
	        end = True
	keys = pg.key.get_pressed()
	if(keys[K_w] and not s):
		w = True
		a = False
		s = False
		d = False
	elif(keys[K_s] and not w):
		w = False
		a = False
		s = True
		d = False  
	elif(keys[K_d] and not a):
		w = False
		a = False
		s = False
		d = True     
	elif(keys[K_a] and not d):
		w = False
		a = True
		s = False
		d = False
	if w: snake.moveUp()
	if a: snake.moveRight()
	if s: snake.moveDown()
	if d: snake.moveLeft()
	gameDisplay.fill((0,0,0))
	if(snake.foodCol(goal.x,goal.y)):
		goal = food()
	snake.updateOld()
	snake.draw(gameDisplay)
	goal.draw(gameDisplay)
	pg.display.update()
	clock.tick(20)
pg.quit()
quit()