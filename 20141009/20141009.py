a = open('thisFile.txt','rU')
q = 0
b = a.read()
c = b

for i,j in enumerate(b):
	if j ==' ':
		q += 1
		if q % 5==0 :
			c = c[:i] + '\n' + c[i+1:]

print c
