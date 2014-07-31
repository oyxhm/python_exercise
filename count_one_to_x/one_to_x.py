#-*-coding:utf-8-*-
#从1加到输入的数字，显示能被输入的数整除的数字和输入数，单数可以，双数不行
import math

a = raw_input("请输入一个正整数：")
a = int(a)
i = 1
sum = 0
for i in range(1, a+1) :
	sum = i + sum
if sum % a == 0 :
	print sum , a
else :
	pass