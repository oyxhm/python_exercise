i = 1
a = raw_input("Please enter an number greater than 2:")
while not a.isdigit() or not float(a) > 2:
	a = raw_input("Please enter an number greater than 2:")

while float(a) > 2 :
	print  i, ':' , '%.3f' %float(a)**0.5
	i += 1
	a = float(a)**0.5
	if a < 2 :
		break


