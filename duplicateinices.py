list1=[]
n=int(input("enter size of list"))
for i in range(0,n):
    x=int(input())
    list1.append(x)
    
v=int(input("enter number to check multiple duplicate index:"))
list2=[i for i in range(0,len(list1)) if list1[i]==v]
print("all the index of",v,"are",list2)