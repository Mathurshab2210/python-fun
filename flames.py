n1=input("enter name 1").lower().replace(" ","")
n2=input("enter name 2").lower().replace(" ","")

for i in n1:
    for j in n2:
        if i==j:
            n1=n1.replace(i,"",1)#1 represents the occurence
            n2=n2.replace(j,"",1)
            break
        
count=len(n1)+len(n2)
print(count)
if count>0:
    list1=["f","l","a","m","e","s"]
    while len(list1)>1:
        c=count%len(list1)
        index=c-1
        print(index)
        if index>=0:
            left=list1[:index]
            right=list1[index+1 : ]
            list1=right+left#for cicular count
            print(list1)
        else:
            list1=list1[: len(list1)-1]   
    print("relationship is:\n",list1[0].upper())
else:
    print("restart the program")
            
    