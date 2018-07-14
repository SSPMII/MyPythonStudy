'''
新建一个学生类
'''
class Student():
	pass
#定义一个对象
pengpeng = Student()
#定义一个Python学生类
class PythonStudent():
	name = None
	age = 18
	course = 'Python'
	def doHomework(self):
		print('我在做作业')
		#推荐在函数末尾使用return
		return None
shenwei = PythonStudent()
print(shenwei.name)
print(shenwei.age)
shenwei.doHomework()
print(shenwei.__dict__)
print(PythonStudent.__dict__)