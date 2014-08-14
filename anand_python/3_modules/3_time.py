import os
import time
f='/home/siva'
a=os.listdir(f)
for i in a:
	x=os.path.getsize(i)
	y=os.path.getatime(i)
	print i,x,y
