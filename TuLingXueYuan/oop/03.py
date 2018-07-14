#__setattr__的使用
class Person():
	def __init__(self):
		pass
	def __setattr__(self, key, value):
		print('设置属性:{0} = {1}'.format(key,value))
		#下面语句会导致死循环
		#self.key = value
		#为避免死循环,规定同意调用父类魔法函数
		super().__setattr__(key, value)
p = Person()
print(p.__dict__)
p.age = 18

# __gt__
class Student():
	def __init__(self, name):
		self._name = name
	def __gt__(self, other):
		print('{0}会比{1}大吗?'.format(self._name, other._name))
		return self._name > other._name
stu1 = Student('one')
stu2 = Student('two')
#字符串的比较按照ascii码顺序比较
print(stu1 > stu2)

