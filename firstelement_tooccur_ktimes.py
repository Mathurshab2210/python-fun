def firstElementKTime(a, n, k):
   for i in a:
       c=0
       for j in a:
           if i==j:
               c=c+1
           if c==k:
               return i

a=[1,2,5,6,5,2,3,2,3,3]
k=2
n=len(a)
print(firstElementKTime(a, n, k))