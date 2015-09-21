#!/usr/bin/python

import pygame
pygame.init()

class Hand():
	def __init__(self):
		#position
		self.pos_x = 0
		self.pos_y = 0

		#say if hand is picking or not
		self.picking = False

		#window
		self.screen = ""
		
	def draw_hand(self):
		pos = pygame.mouse.get_pos()
		self.pos_x = pos[0]
		self.pos_y = pos[1]

		if self.picking:
			hand = pygame.image.load("../images/pick.png")
			(self.screen).blit(hand, (self.pos_x, self.pos_y))
		else:
			hand = pygame.image.load("../images/open.png")
			(self.screen).blit(hand, (self.pos_x, self.pos_y))
			
			
		
