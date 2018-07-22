import unittest
from city_functions import city_format


class NameTestCase(unittest.TestCase):
	'''测试city_functions.py'''

	def test_city_country(self):
		'''能正确处理像shanghai,china这样的实例吗?'''

		formated_city = city_format('shanghai', 'china', 2.4e7)
		self.assertEqual(formated_city, 'Shanghai, China - Population 24000000.0')


unittest.main