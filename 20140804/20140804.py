#-*-coding:utf-8-*-
#���ڵ�λת���ͷ������
import math

input = raw_input("���������ж���ͭ��")
input = int(input)
c = input % 100
a = input / 10000
b = (input - a*10000) / 100


if a == 0 :
	if b == 0:
		if c == 0:
			print 'ûǮ�����˿'
		else :
			print c ,'ͭ'
	else:
		if c == 0:
			print b, '��'
		else :
			print b ,'��' ,c , 'ͭ'
else:
	if b == 0:
		if c == 0:
			print a , '��'
		else :
			print a , '��' ,c ,'ͭ'
	else:
		if c == 0:
			print a , '��', b , '��'
		else :
			print a ,'��' ,b ,'��', c, 'ͭ' 


