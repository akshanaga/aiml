import pandas as p 
from functools import reduce
d={'numbers':[1,2,3,4,5],'letters':['a','b','c','d','e']}
di=p.DataFrame(d)
sq=di['numbers'].map(lambda x:x**2)
ev=list(filter(lambda x:x%2==0,di['numbers']))
pr=reduce(lambda x,y:x+y,di['numbers'])
print("DataFrame:",d)
print("\n mapping:",sq)
print("\n filtering:",ev)
print("\n reducing:",pr)