#!/usr/bin/python

import pygame
pygame.init()

import math

from class_littleguy import *
from class_hand import *

BLACK = (0x00, 0x00, 0x00)
WHITE = (0xFF, 0xFF, 0xFF)
GREEN = (0x00, 0xFF, 0x00)
RED = (0xFF, 0x00, 0x00)
SKIN_WHITE = (0xE8, 0xCD, 0xA8)

# little guy's position
pos = pygame.mouse.get_pos()
pos_x = 350
pos_y = 500
pygame.mouse.set_visible(False)

# little guy's direction and speed
change_x = 20
change_y = 20

# timer to blink
blink_timer = 0

# set screen size
size = (1000, 700)
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

#littleguy2 = Littleguy()
#littleguy2.screen = screen
#littleguy2.pos_x = pos_x
#littleguy2.pos_y = pos_y
#littleguy2.explode = False
#littleguy2.img_choice = 1

# rotate body
littleguy.body_angle = "center"

# god's hand
hand = Hand()
hand.screen = screen
positionToPick = False #well positined above little guy

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
			if event.key == pygame.K_DOWN and littleguy.pos_y < 380:
				littleguy.pos_y += change_y
			if event.key == pygame.K_SPACE:
				hand.picking = True
				littleguy.explode = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				hand.picking = False
				positionToPick = False
				littleguy.explode = False
				littleguy.explode_timer = 0
			if event.key == pygame.K_LEFT:
				littleguy.body_angle = "center"
			if event.key == pygame.K_RIGHT:
				littleguy.body_angle = "center"

	if hand.picking and (not positionToPick):
		if ((littleguy.pos_x - 10) < (hand.pos_x + 65)) and ((littleguy.pos_x + 10) > (hand.pos_x + 65)) and ((littleguy.pos_y - 10) < (hand.pos_y + 230)) and ((littleguy.pos_y + 10) > (hand.pos_y + 230)):
			positionToPick = True
				
	#get current key pressed
	keys = pygame.key.get_pressed()
	if not hand.picking:
		if keys[pygame.K_LEFT]:
			littleguy.pos_x -= change_x
		if keys[pygame.K_RIGHT]:
			littleguy.pos_x += change_x
		if keys[pygame.K_UP]:
			littleguy.pos_y -= change_y
		elif littleguy.pos_y < 450:
			littleguy.pos_y += change_y
		if keys[pygame.K_DOWN] and littleguy.pos_y < 680:
			littleguy.pos_y += change_y
	if hand.picking and positionToPick:
		littleguy.explode_timer += 5
		littleguy.pos_x = hand.pos_x + 65
		littleguy.pos_y = hand.pos_y + 230
	

	#--position for little guy 2
	pos = pygame.mouse.get_pos()
	#littleguy2.pos_x = pos[0]
	#littleguy2.pos_y = pos[1]
	#--------------------------------------------------

	#-------GAME LOGIC---------------------------------
	blink_timer += 1
	#-------------------------------------------------

	#---------DRAWING--------------------------------
	# background
	#screen.fill(WHITE)
	background = pygame.image.load("../images/background.png")
	screen.blit(background, (0, 0))

	# little guy's face
	if blink_timer < 80:
		littleguy.img_choice = 1
		littleguy.draw_face()
		#littleguy2.draw_face()
	if blink_timer >= 80:
		littleguy.img_choice = 2
		littleguy.draw_face()
		#littleguy2.draw_face()
		if blink_timer > 100:
			blink_timer = 0
	hand.draw_hand();
	

	#update screen
	pygame.display.flip()
	#------------------------------------------------
