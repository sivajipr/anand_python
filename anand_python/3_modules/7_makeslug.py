import re
def makeslug(a):
	b=re.findall('\w+',a)
	print ('-').join(b)
makeslug('!hello world@  #$')
