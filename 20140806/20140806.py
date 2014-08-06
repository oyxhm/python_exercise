import math

first = 0

for a in range(1,10):
	for b in range(1,a+1):
		first += b * 10**(a-b)
	print str(first) + ' * 8 + ' + str(a) + ' = ' + str(first*8+a)
	first = 0
	
for a in range(1,10):
	for b in range(1,a+1):
		first += b * 10**(a-b)
	print str(first) + ' * 9 + ' + str(a+1) + ' = ' + str(first*9+(a+1))
	first = 0
	
for a in range(9,1,-1):
	for b in range(0,10-a):
		first +=  (a+b) * 10**b
	print str(first) + ' * 9 + ' + str(a-2) + ' = ' + str(first*9+(a-2))
	first = 0
	
for a in range(0,9):
	for b in range(0,a+1):
		first += 1 * 10**b	
	print str(first) + ' * ' + str(first) + ' = ' + str(first**2)
	first = 0
	




