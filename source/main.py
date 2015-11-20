#!/usr/bin/python

import pygame
pygame.init()

import math
from class_littleguy import *
from class_hand import *
#import bad_gpio_read as IOREAD
from get_accel import *

WHITE = (0xFF, 0xFF, 0xFF)

# little guy's position
pos = pygame.mouse.get_pos()
pos_x = 350
pos_y = 500
pygame.mouse.set_visible(False)

# little guy's direction and speed
change_x = 50
change_y = 50
# hand's direction and speed
hand_change_x = 25
hand_change_y = 25

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

# rotate body
littleguy.body_angle = "center"

# god's hand
hand = Hand()
hand.screen = screen
positionToPick = False #well positined above little guy
move_range_x = 0.2
move_range_y = 0.2

while not done:
	#force = IOREAD.get_force()
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
	"""
	if (force == 2):
		hand.picking = True
	else:
		hand.picking = False
		littleguy.explode = False
		positionToPick = False
	"""	

	try :
		# move in x-axis
		if (accel_scaled_x() > move_range_x and hand.pos_x < 800):
			if (accel_scaled_x() > 4 * move_range_x):
				hand.pos_x += hand_change_x
			hand.pos_x += hand_change_x
		elif (accel_scaled_x() < -move_range_x and hand.pos_x > 0):
			if (accel_scaled_x() < -4 * move_range_x):
				hand.pos_x -= hand_change_x
			hand.pos_x -= hand_change_x

		# move in y-axis
		if (accel_scaled_y() > move_range_y and hand.pos_y < 500):
			if (accel_scaled_y() > 4 * move_range_y):	
				hand.pos_y += hand_change_y
			hand.pos_y += hand_change_y
		elif (accel_scaled_y() < -move_range_y and hand.pos_y > 0):
			if (accel_scaled_y() < -4 * move_range_y):	
				hand.pos_y -= hand_change_y
			hand.pos_y -= hand_change_y
	except:
		pass
		
	# gets if hand is well positioned to pick guy
	if hand.picking and (not positionToPick):
		if ((littleguy.pos_x - 10) < (hand.pos_x + 32)) and ((littleguy.pos_x + 10) > (hand.pos_x + 32)) and ((littleguy.pos_y - 10) < (hand.pos_y + 115)) and ((littleguy.pos_y + 10) > (hand.pos_y + 115)):
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
		if keys[pygame.K_DOWN] and littleguy.pos_y < 680:
			littleguy.pos_y += change_y
	if hand.picking and positionToPick:
		#littleguy.explode_timer += 5
		#littleguy.explode_timer = force
		littleguy.pos_x = hand.pos_x + 32
		littleguy.pos_y = hand.pos_y + 115
	elif littleguy.pos_y < 500:
		littleguy.pos_y += change_y
	

	#-------GAME LOGIC---------------------------------
	blink_timer += 1
	#-------------------------------------------------

	#---------DRAWING--------------------------------
	# background
	#screen.fill(WHITE)
	background = pygame.image.load("../images/background.jpg").convert()
	screen.blit(background, (0, 0))

	# little guy's face
	if blink_timer < 80:
		littleguy.img_choice = 1
		littleguy.draw_face()
	if blink_timer >= 80:
		littleguy.img_choice = 2
		littleguy.draw_face()
		if blink_timer > 100:
			blink_timer = 0
	hand.draw_hand();
	

	#update screen
	pygame.display.flip()
	#------------------------------------------------
