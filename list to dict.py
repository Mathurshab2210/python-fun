list1=[]
list2=[]
n=int(input("enter size for list1"))
for i in range(0,n):
    x=input("enter items here:")
    list1.append(x)

m=int(input("enter size for list2"))
for i in range(0,m):
    y=input("enter items here:")
    list2.append(y)
    
con=dict(zip(list1,list2))

print(con)