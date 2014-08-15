import math

print 'y = ax2 + bx + c'
a = raw_input("Please input a:")
b = raw_input("Please input b:")
c = raw_input("Please input c:")
a = float(a)
b = float(b)
c = float(c)
delta = b**2 - 4*a*c
if delta < 0 :
		print 'x1 = '  ,-b/(2*a) ,'+' ,(-delta)**0.5/(2*a) , 'j'
		print 'x2 = '  ,-b/(2*a) ,'-' ,(-delta)**0.5/(2*a) , 'j'
elif delta == 0 :
	print 'x =' ,-b/(2*a)
else :
	print 'x1 = ' , (-b + delta**0.5) / (2*a)
	print 'x2 = ' , (-b - delta**0.5) / (2*a)
	