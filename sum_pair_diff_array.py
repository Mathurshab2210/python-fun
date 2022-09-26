def sumpair(a,b,n,m,s):
    for i in range(0,n):
        for j in range(0,m):
            if a[i]+b[j] == s:
                print(a[i],b[j])
                
            
a=[1,2,3,6,5]
b=[2,3,4,8,9]
n=len(a)
m=len(b)
s=8
if n==m:
    sumpair(a,b,n,m,s)
else:
    print('len is not equal')
