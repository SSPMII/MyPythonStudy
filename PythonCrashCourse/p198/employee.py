class Employee():
	'''创建一个雇员类'''

	def __init__(self, first_name, last_name, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, salary_raised=5000):
		self.salary += salary_raised




