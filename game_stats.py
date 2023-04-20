class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = ai_settings.ship_limit
		
		# Start Alien Invation in an active state
		self.game_active = True
