#一直提示要求输入整数。就像验证码一样，输不对就一直弹出页面要求你重新输入。
input = raw_input("Input an integer:")
while not input.isdigit() :
	print 'Error , try again.'
	input = raw_input("Input an integer:")
print 'The integer is :' , input
	