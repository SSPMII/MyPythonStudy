# 用户
class User():
	def __init__(self, first_name, last_name, **others):
		self.first_name = first_name
		self.last_name = last_name
		self.others = others
		self.login_attempts = 0
	#打印用户信息
	def describe_users(self):
		print('User infomation: ' +
		      '- ' + str(self.first_name).title() + ' ' + str(self.last_name).title())
	#个性化问候
	def greet_users(self):
		print('Hello ' + str(self.first_name).title() + ' ' + str(self.last_name).title())
	#尝试登录次数
	def increment_login_attempts(self):
		self.login_attempts += 1
	#重置登录次数
	def reset_login_attempts(self):
		self.login_attempts = 0

#实例化
user1 = User('max','well')
user1.greet_users()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
