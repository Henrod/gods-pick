#!/usr/bin/python

import pygame
pygame.init()

class Littleguy():
	def __init__(self):
		# select type of head
		self.img_choice = 0
		self.body_angle = "center"

		# new window
		self.screen = ""

		# timer to explode head
		self.explode = False
		self.explode_timer = 0

		# position of character
		self.pos_x = 0
		self.pos_y = 0

		# keeps the last position to compare
		self.last_pos_x = 0
	
	def draw_face(self):
		pos = pygame.mouse.get_pos()
		#self.pos_x = pos[0]
		#self.pos_y = pos[1]

		if not self.explode:
			if self.img_choice == 1:
				face = pygame.image.load("../images/littleguy.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			if self.img_choice == 2:
				face = pygame.image.load("../images/littleguy_blink.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
		if self.explode:
			if self.explode_timer == 1: #< 100:
				face = pygame.image.load("../images/littleguy_blink.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			if self.explode_timer == 2: #>= 100 and self.explode_timer < 200:
				face = pygame.image.load("../images/littleguy_explode1.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			if self.explode_timer == 3: #>= 200:
				face = pygame.image.load("../images/littleguy_explode2.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			
		body = pygame.image.load("../images/littleguy_body.png")
		if self.body_angle == "left" or self.last_pos_x > self.pos_x:
			body_surf = pygame.transform.rotate(body, 45)
			(self.screen).blit(body_surf, (self.pos_x + 5 , self.pos_y + 15))
		elif self.body_angle == "right" or self.last_pos_x < self.pos_x:
			body_surf = pygame.transform.rotate(body, -45)
			(self.screen).blit(body_surf, (self.pos_x - 15 , self.pos_y + 20))
		else: 
			body_surf = pygame.transform.rotate(body, 0)
			(self.screen).blit(body_surf, (self.pos_x + 5, self.pos_y + 25))

		self.last_pos_x = self.pos_x
