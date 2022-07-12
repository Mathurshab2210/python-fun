a=[1,2,4,5,6,7]
x1=a[0]
for i in range(1,len(a)):
    x1=x1^a[i]
    
x2=0
for i in range(0,len(a)+2):
    x2=x2^i
    
result=x1^x2
print(result)
