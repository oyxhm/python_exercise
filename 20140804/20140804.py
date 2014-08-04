#-*-coding:utf-8-*-
#关于单位转换和非零输出
import math

input = raw_input("请输入你有多少铜：")
input = int(input)
c = input % 100
a = input / 10000
b = (input - a*10000) / 100


if a == 0 :
	if b == 0:
		if c == 0:
			print '没钱的穷屌丝'
		else :
			print c ,'铜'
	else:
		if c == 0:
			print b, '银'
		else :
			print b ,'银' ,c , '铜'
else:
	if b == 0:
		if c == 0:
			print a , '金'
		else :
			print a , '金' ,c ,'铜'
	else:
		if c == 0:
			print a , '金', b , '银'
		else :
			print a ,'金' ,b ,'银', c, '铜' 


