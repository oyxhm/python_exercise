#SEND+MORE = MONEY
def clear(i):
	return str(i)

for a in range(1000,10000):
	for b in range(1000,10000):
		c = a + b
		if c >= 10000:
			a = clear(a)
			b = clear(b)
			c = clear(c)
			if 	a[1] == b[3] and b[0] == c[0] and b[1] == c[1] and a[2] == c[2] and b[3] == c[3]:
				print c