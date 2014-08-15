#-*-coding:utf-8-*-
import math

a = raw_input("请输入一个数：")
a = int(a)
b = 2
flag = 0

for b in range(2,int(a**0.5)+1):
	c = a % b
	if c == 0:
		flag = 1
		break
if flag :
	print a,'不是素数'
else :
	print a,'是素数'