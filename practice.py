
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.hours = ' '
		
	def describe_restaurant(self):
		"""Print two pieces of information about the restaurant."""
		print("Our restaurant name is " + str(self.restaurant_name) + ".")
		print("\nThe cuisine type is " + str(self.cuisine_type) + ".")
		
	def open_restaurant(self):
		"""Print a message indicating when the restaurant is open."""
		self.hours = {'Open': '(11 a.m. to 3 a.m.)', 'Closed': '(3 a.m. to 11 a.m.)'}
		print("\nWe are " + str(self.hours) + "!")

customer1 = Restaurant('Misses', 'Italian')
customer1.Restaurant()
0
