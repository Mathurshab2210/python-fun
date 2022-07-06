str=input("enter string: \n")
x=input("Enter the charecter to find the mid ocuurence\n")
ind=[]
for idx,ele in enumerate(str):
    if(ele==x):
        ind.append(idx)
        
res=ind[len(ind)//2]
print(res)