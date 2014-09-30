import os 

a = open('thisFile.txt','rU')

count = len(a.readlines())

for i in range(count):
    sheet = []
    if (i*2+1) < count:
        a.seek(0)    
        sheet.append(a.readlines()[i*2+1])
        b = open('thatFile.txt','a')
    	b.write(sheet[0])
b.close()    
