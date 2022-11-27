n=int(input('enter num'))
f=0
a=[]
for i in range(2,n+1):
    if(n%i==0):
        for j in range(2,i//2):
            if(i%j==0):
                f=1
                break
        if f==0:
            print(i)
            a.append(i)
            print(a)
            print(sum(a))
            
    