import collections
from collections import Counter
l=[1,2,2,8,7,7,5]
l=sorted(l)
c=Counter(l)
for k,v in c.most_common():
   if c[v] > 1:
       print(k,v)
       
       
for x in l:
    if l.count(x) > 1:
        print(x)