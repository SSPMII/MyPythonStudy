# _*_ coding: utf-8 _*_ 
def move(n,a,b,c):
	if n == 1:
		print(a, '-->', c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(1, 'A', 'B', 'C')

'''
期待输出：
A --> C
A --> B
C --> B
A --> C
B --> A
B --> C
A --> C
'''