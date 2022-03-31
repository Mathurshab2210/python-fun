import random
list1=[]
n=int(input("Enter number of friends"))
for i in range(0,n):
    list1.append(input("enter friends name"))
list2=[]
for i in range(n):
    list2.append(int(input(f'enter salary of {i} friend')))
    
m=random.randint(0,n-1)
print(list2[m])
end=False
while not end:
    if list2[m]>1500:
        print(f'{list1[m]} will give party today')
        end=True
    else:
        q=random.randint(0,n-1)
        print(f'{list1[q]} will give party today')
        end=True
       
  #random person selection on the basis of a threshold deciding value
    
     
