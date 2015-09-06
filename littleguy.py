#!/usr/bin/python

import pygame
pygame.init()

BLACK = (0x00, 0x00, 0x00)
WHITE = (0xFF, 0xFF, 0xFF)
GREEN = (0x00, 0xFF, 0x00)
RED = (0xFF, 0x00, 0x00)
SKIN_WHITE = (0xE8, 0xCD, 0xA8)

def draw_face():
	img = pygame.image.load("littleguy.png")
	screen.blit(img, (0, 0))
#	pygame.draw.ellipse(screen, SKIN_WHITE, [50, 50, 50, 100])
#	for i in range (12):
#		pygame.draw.line(screen, BLACK, [50+2*i, 80-i], [50+2*i, 30-i], 2)
#	pygame.draw.line(screen, BLACK, [74, 67], [74, 17], 2)
#	for i in range (12):
#		pygame.draw.line(screen, BLACK, [75+2*i, 68+i], [75+2*i, 18+i], 2)

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
	#--------MAIN EVENT LOOP----------------------------
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:	
				done = True
	#--------------------------------------------------

	#-------GAME LOGIC---------------------------------
	#-------------------------------------------------

	#---------DRAWING--------------------------------
	# background
	screen.fill(WHITE)

	# little guy's face
	draw_face()

	#update screen
	pygame.display.flip()
	#------------------------------------------------
