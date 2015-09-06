#!/usr/bin/python

import pygame
pygame.init()

BLACK = (0x00, 0x00, 0x00)
WHITE = (0xFF, 0xFF, 0xFF)
GREEN = (0x00, 0xFF, 0x00)
RED = (0xFF, 0x00, 0x00)
SKIN_WHITE = (0xE8, 0xCD, 0xA8)

# set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)
# set screen title
pygame.display.set_caption("Little Guy")

# boolean to continue loop
done = False

# manage how fast the screen updates
clock = pygame.time.Clock()

while not done:
	#--------MAIN LOOP
	#-----------------

	#-------GAME LOGIC
	#-----------------

	#---------DRAwING
	# background
	screen.fill(WHITE)

	# little guy's face
		pygame.draw.ellipse(screen, SKIN_WHITE, [50, 50, 50, 100])

	#update screen
	pygame.display.flip()
	#----------------
