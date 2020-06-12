import pygame,sys, os
from pygame.locals import *

red=(255,0,0)
catx=10
caty=10
screen=0

def myquit():
	pygame.quit()
	sys.exit(0)

def check_inputs(events):
	global catx,caty,screen

	for event in events:
		if event.type == QUIT:
			quit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				quit()
			elif event.key == K_UP:
				caty-=5
				print('UP')
			elif event.key == K_DOWN:
				caty+=5
				print('DOWN')
			elif event.key == K_LEFT:
				catx-=5
				print('LEFT')
			elif event.key == K_RIGHT:
				catx+=5
				print('RIGHT')
	screen=pygame.display.get_surface()
	screen.fill((0,0,0))
	pygame.draw.rect(screen,(255,255,255),(catx,caty,50,50))
	pygame.display.update()



def main():
	pygame.init()
	window=pygame.display.set_mode((1024,720))
	pygame.display.set_caption("Snake")

	screen=pygame.display.get_surface()
	screen.fill(red)

	pygame.display.flip()

	while True:
	    check_inputs(pygame.event.get())

main()
