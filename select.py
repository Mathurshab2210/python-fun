import random
list1=[]
n=int(input("Enter number of friends"))
for i in range(0,n):
    list1.append(input("enter friends name"))

m=random.randint(0,n)
print(f"{list1[m]} will give party today")
     
