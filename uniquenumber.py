list1=[]
n=int(input("enter size of list"))
for i in range(0,n):
    x=int(input())
    list1.append(x)
    
    

flist=[]
for ele in list1:
    if ele not in flist:
        flist.append(ele)
        
print(flist)