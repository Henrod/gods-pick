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
	
	def draw_face(self):
		pos = pygame.mouse.get_pos()
		#pos_x = pos[0]
		#pos_y = pos[1]

		if not self.explode:
			if self.img_choice == 1:
				face = pygame.image.load("littleguy.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			if self.img_choice == 2:
				face = pygame.image.load("littleguy_blink.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
		if self.explode:
			if self.explode_timer < 1000:
				face = pygame.image.load("littleguy_blink.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			if self.explode_timer >= 1000 and self.explode_timer < 2000:
				face = pygame.image.load("littleguy_explode1.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			if self.explode_timer >= 2000:
				face = pygame.image.load("littleguy_explode2.png")
				(self.screen).blit(face, (self.pos_x, self.pos_y))
			
		body = pygame.image.load("littleguy_body.png")
		if self.body_angle == "center":
			body_surf = pygame.transform.rotate(body, 0)
			(self.screen).blit(body_surf, (self.pos_x + 10, self.pos_y + 50))
		if self.body_angle == "left":
			body_surf = pygame.transform.rotate(body, 45)
			(self.screen).blit(body_surf, (self.pos_x + 10 , self.pos_y + 30))
		if self.body_angle == "right":
			body_surf = pygame.transform.rotate(body, -45)
			(self.screen).blit(body_surf, (self.pos_x - 30 , self.pos_y + 40))
