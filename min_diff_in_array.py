a=[1,5,47,6,35,7,4]
a.sort()
print(a)
flist=[]
for i in range (0,len(a)):
    for j in range(i+1,len(a)):
        x=a[j]-a[i]
        print(x)
        flist.append(x)

flist.sort()
print(flist[0])