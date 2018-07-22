# 加法运算
while True:
	try:
		number1 = int(input('第一个数字: '))
		number2 = int(input('第二个数字: '))
	except ValueError:
		print('给老子输入整数!')
		continue
	else:
		print('{0} + {1} = {2}'.format(number1, number2, number1+number2))
		break