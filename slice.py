# -*- coding: utf-8 -*-
def trim(s):
	while s[:1] == ' ':
		s = s[1:]
	while s[-1:] == ' ':
		s = s[:-2]
	return s





# 测试:
print(trim('  hello  world  '))
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')