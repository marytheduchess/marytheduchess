## Chapter 15 "Generating Data"; Data Visualization Project II
import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ships import Ship
from alien import Alien
import game_functions as gf

def run_game():
	# Initialize pygame, settings and screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))	
	screen = pygame.display.set_mode((1000, 725))
	pygame.display.set_caption("Alien Invasion")
	
	# Make a ship, a group of bullets and a group of aliens
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets in.
	bullets = Group()
	aliens = Group()
	# Set the background color.
	bg_color = (230, 230, 230)
	# Make an alien.
	alien = Alien(ai_settings, screen)
	# Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, aliens)
	
	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)	
		gf.update_screen(ai_settings, screen, ship, alien, bullets)
		# Get rid of bullets that have disappeared.
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))
				
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit() 
		# Redraw the screen during each pass through the loop.
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		

			
		# Make the most recently drawn screen visible
		pygame.display.flip()
		
run_game()


 

