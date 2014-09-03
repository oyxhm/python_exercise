def clear(i):
	if i < 10:
		return  '00000' + str(i)
	elif i < 100 and i >= 10:
		return  '0000' + str(i)
	elif i < 1000 and i >= 100:
		return  '000' + str(i)
	elif i < 10000 and i >= 1000:
		return  '00' + str(i)
	elif i < 100000 and i >= 10000:
		return  '0' + str(i)
	else:
		return  str(i)
	

for i in range(1,1000000):
	i = clear(i)
	if i[2] == i[5] and i[3] == i[4]:
		i = int(i) + 1
		i = clear(i)
		if i[1] == i[5] and i[2] == i[4]:			
			i = int(i) + 1
			i = clear(i)
			if i[1] == i[4] and i[2] == i[3]:
				i = int(i) + 3
				i = clear(i)
				if i[0] == i[5] and i[1] == i[4] and i[2] == i[3]:
					print int(i) - 5			
