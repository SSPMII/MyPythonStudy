#三种方法
class Person():
	#实例方法
	def eat(self):
		print(self)
		print('Eating......')

	#类方法
	#类方法的第一个参数,一般命名为cls,区别与self
	@classmethod
	def play(cls):
		print('Playing......')

	#静态方法
	#不需要第一个参数表示自身或者类
	@staticmethod
	def say():
		print('Saying......')

shenwei = Person()

#实例方法
shenwei.eat()
#类方法
Person.play()
shenwei.play()
#静态方法
Person.say()
shenwei.say()
