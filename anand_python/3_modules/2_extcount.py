import os
b=[]
c=[]
x=[]
y=[]
z=[]
d=[]
dir='/home/siva/python'
a=os.listdir(dir)
def uni(y):
	for i in y:
		if i not in z:
			z.append(i)
	return z
def join(a,b):
	return[(x,y)for x in a for y in b if a.index(x)==b.index(y)]
for i in a:
	b.append(i.split('.'))
for i in b:
	c.append(i[1])
for i in c:
	x.append(c.count(i))
for i in uni(join(x,c)):
	print i
