#factorial of a number
def fact(a):
	n=1
	for i in range(1,a+1):
		n=n*i
	print n
fact(4)
