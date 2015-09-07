#!/usr/bin/python

import pygame
pygame.init()

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

# timer to explode
explode_timer = 0
explode = False

# rotate body
body_angle = "center"

def draw_face(img_choice, angle):
	pos = pygame.mouse.get_pos()
	#pos_x = pos[0]
	#pos_y = pos[1]

	if not explode:
		if img_choice == 1:
			face = pygame.image.load("littleguy.png")
			screen.blit(face, (pos_x, pos_y))
		if img_choice == 2:
			face = pygame.image.load("littleguy_blink.png")
			screen.blit(face, (pos_x, pos_y))
	if explode:
		if explode_timer < 2000:
			face = pygame.image.load("littleguy_blink.png")
			screen.blit(face, (pos_x, pos_y))
		if explode_timer >= 2000 and explode_timer < 4000:
			face = pygame.image.load("littleguy_explode1.png")
			screen.blit(face, (pos_x, pos_y))
		if explode_timer >= 4000:
			face = pygame.image.load("littleguy_explode2.png")
			screen.blit(face, (pos_x, pos_y))
		
	body = pygame.image.load("littleguy_body.png")
	if angle == "center":
		body_surf = pygame.transform.rotate(body, 0)
		screen.blit(body_surf, (pos_x + 10, pos_y + 50))
	if angle == "left":
		body_surf = pygame.transform.rotate(body, 45)
		screen.blit(body_surf, (pos_x + 10 , pos_y + 30))
	if angle == "right":
		body_surf = pygame.transform.rotate(body, -45)
		screen.blit(body_surf, (pos_x - 30 , pos_y + 40))
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
			if event.key == pygame.K_LEFT:
				pos_x -= change_x
				body_angle = "left"
			if event.key == pygame.K_RIGHT:
				pos_x += change_x
				body_angle = "right"
			if event.key == pygame.K_UP:
				pos_y -= change_y
			if event.key == pygame.K_DOWN:
				pos_y += change_y
			if event.key == pygame.K_SPACE:
				explode = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				explode = False
				explode_timer = 0
			if event.key == pygame.K_LEFT:
				body_angle = "center"
			if event.key == pygame.K_RIGHT:
				body_angle = "center"
	#get current key pressed
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		pos_x -= change_x
	if keys[pygame.K_RIGHT]:
		pos_x += change_x
	if keys[pygame.K_UP]:
		pos_y -= change_y
	if keys[pygame.K_DOWN]:
		pos_y += change_y
	if keys[pygame.K_SPACE]:
		explode_timer += 1
	#--------------------------------------------------

	#-------GAME LOGIC---------------------------------
	blink_timer += 1
	#-------------------------------------------------

	#---------DRAWING--------------------------------
	# background
	screen.fill(WHITE)

	# little guy's face
	if blink_timer < 3000:
		draw_face(1, body_angle)
	if blink_timer >= 3000:
		draw_face(2, body_angle)
		if blink_timer > 3500:
			blink_timer = 0

	#update screen
	pygame.display.flip()
	#------------------------------------------------
