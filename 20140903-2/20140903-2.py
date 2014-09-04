
for i in range(10,100):
	result = i**2
	a = result/100
	b = result - a*100
	if b == i:
		print i
