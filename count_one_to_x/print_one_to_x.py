#-*-coding:utf-8-*-
import math

a = raw_input("请输入一个正整数：")
a = int(a)
i = 1
sum = 0
for i in range(a + 1) :
	sum = i + sum
print sum