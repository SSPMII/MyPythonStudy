# _*_ coding utf-8 _*_

h = input ('请输入你的身高（米）')
height = float(h)
w = input ('请输入你的体重（千克）')
weight = float(w)
bmi = weight / height **2
print('BMI = %.1f' %bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')