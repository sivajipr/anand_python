#zip function using list compreensions
a=['a','b','c']
b=[1,2,3]
print [(x,y) for x in a for y in b if a.index(x)==b.index(y)]
