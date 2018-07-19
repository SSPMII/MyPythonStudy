# p142页类习题
class Restaurant():
	'餐馆'
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print('The ' + self.restaurant_name + ' has ' + self.cuisine_type)

	def open_restaurant(self):
		print('Opening...')

restaurant = Restaurant('KFC', 'fried chicken')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
