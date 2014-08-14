#implementation of map using list comprehension
def square(a):
	return a*a
m=[]
def map(n):
	for i in n:
		m.append(square(i))
	print m
map(range(5))
