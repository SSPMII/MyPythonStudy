# _*_ coding: utf-8 _*_
#小明的成绩从去年的72分提升到了今年的85分，
#请计算小明成绩提升的百分点，
#并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1 = 72
s2 = 85
r = (s2 - s1)/s2*100
print('%.1f%%' %r )