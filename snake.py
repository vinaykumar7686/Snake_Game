import pygame,sys, os
from pygame.locals import *

red=(255,0,0)


def check_inputs(events):
	global catx,caty,screen

	for event in events:
		if event.type == QUIT:
			quit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				quit()
			elif event.key == K_UP:
				print('UP')
			elif event.key == K_DOWN:
				print('DOWN')
			elif event.key == K_LEFT:
				print('LEFT')
			elif event.key == K_RIGHT:
				print('RIGHT')




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
