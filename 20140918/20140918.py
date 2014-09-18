prize_red = [11,14,17,22,25,27]
prize_blue = 26
yournum = range(6)
yournum[0] = raw_input('Please input your red number1:')
yournum[1] = raw_input('Please input your red number2:')
yournum[2] = raw_input('Please input your red number3:')
yournum[3] = raw_input('Please input your red number4:')
yournum[4] = raw_input('Please input your red number5:')
yournum[5] = raw_input('Please input your red number6:')
yourbluenum = raw_input('Please input your blue number:')

r = 0

for i in prize_red : 
	q = 0
	while(q<=5):
		if int(yournum[q]) == i :
			r += 1
		q += 1

b = 0
if prize_blue == int(yourbluenum) :
	b = 1
	
if r == 6 and b == 1 :
	print 'You got 1000w'
elif r == 6 and b == 0 :
	print 'You got 500w'
elif r == 5 and b == 1 :
	print 'You got 3000'
elif r == 5 and b == 0 :
	print 'You got 200'
elif r == 4 and b == 1 :
	print 'You got 200'
elif r == 4 and b == 0 :
	print 'You got 10'
elif r == 3 and b == 1 :
	print 'You got 10'
elif r == 2 and b == 1 :
	print 'You got 5'
elif r == 1 and b == 1 :
	print 'You got 5'
elif r == 0 and b == 1 :
	print 'You got 5'
else :
	print 'thank you'