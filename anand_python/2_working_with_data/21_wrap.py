#Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width
f=open('z.txt','r')
a=f.readlines()
def wrap(a,n):
	for i in a:
		m=0
		for j in a:
			print(i[m:m+n])
			m=m+n
wrap(a,30)
