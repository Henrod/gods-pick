#!/usr/bin/python

import pygame
pygame.init()

from class_littleguy import *

BLACK = (0x00, 0x00, 0x00)
WHITE = (0xFF, 0xFF, 0xFF)
GREEN = (0x00, 0xFF, 0x00)
RED = (0xFF, 0x00, 0x00)
SKIN_WHITE = (0xE8, 0xCD, 0xA8)

# little guy's position
pos = pygame.mouse.get_pos()
pos_x = pos[0]
pos_y = pos[1]
pygame.mouse.set_visible(False)

# little guy's direction and speed
change_x = 1
change_y = 1

# timer to blink
blink_timer = 0

# set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)
# set screen title
pygame.display.set_caption("Little Guy")

# boolean to continue loop
done = False

# manage how fast the screen updates
clock = pygame.time.Clock()

# import littlguy class and initialize it
littleguy = Littleguy()
littleguy.screen = screen
littleguy.pos_x = pos_x
littleguy.pos_y = pos_y
# rotate body
littleguy.body_angle = "center"

while not done:
	#--------MAIN EVENT LOOP----------------------------
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:	
				done = True
			if event.key == pygame.K_LEFT:
				littleguy.pos_x -= change_x
				littleguy.body_angle = "left"
			if event.key == pygame.K_RIGHT:
				littleguy.pos_x += change_x
				littleguy.body_angle = "right"
			if event.key == pygame.K_UP:
				littleguy.pos_y -= change_y
			if event.key == pygame.K_DOWN:
				littleguy.pos_y += change_y
			if event.key == pygame.K_SPACE:
				littleguy.explode = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				littleguy.explode = False
				littleguy.explode_timer = 0
			if event.key == pygame.K_LEFT:
				littleguy.body_angle = "center"
			if event.key == pygame.K_RIGHT:
				littleguy.body_angle = "center"
	#get current key pressed
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		littleguy.pos_x -= change_x
	if keys[pygame.K_RIGHT]:
		littleguy.pos_x += change_x
	if keys[pygame.K_UP]:
		littleguy.pos_y -= change_y
	if keys[pygame.K_DOWN]:
		littleguy.pos_y += change_y
	if keys[pygame.K_SPACE]:
		littleguy.explode_timer += 1
	#--------------------------------------------------

	#-------GAME LOGIC---------------------------------
	blink_timer += 1
	#-------------------------------------------------

	#---------DRAWING--------------------------------
	# background
	screen.fill(WHITE)

	# little guy's face
	if blink_timer < 3000:
		littleguy.img_choice = 1
		littleguy.draw_face()
	if blink_timer >= 3000:
		littleguy.img_choice = 2
		littleguy.draw_face()
		if blink_timer > 3500:
			blink_timer = 0

	#update screen
	pygame.display.flip()
	#------------------------------------------------
