import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
	'''针对employee类的测试'''


	def setUp(self):
		'''创建一个实例供测试'''

		self.me = Employee('Max', 'Well', 100000)


	def test_give_default_raise(self):
		'''测试默认年薪增加'''

		self.me.give_raise()
		self.assertEqual(self.me.salary, 105000)

	def test_give_custom_raise(self):
		'''测试自定义增加'''

		self.me.give_raise(10000)
		self.assertEqual(self.me.salary, 110000)





