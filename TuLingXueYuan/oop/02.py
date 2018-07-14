# property案例
# 定义一个person类,具有name,age属性
# 姓名以大写方式保存
# 年龄以整数保存
# x = property(fget, fset, fdel,doc)

class Person():
	# 函数名称随意
	def fget(self):
		return self._name *2

	def fset(self, name):
		#以大写保存
		self._name = name.upper()

	def fdel(self):
		self._name = 'NoName'

	name = property(fget, fset, fdel, '对name进行操作')

p1 = Person()
p1.name = 'Shenwei'
print(p1.name)
