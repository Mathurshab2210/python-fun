a=[1,2,4,5,6]
n=int(input("enter the first position"))
m=int(input("enter the first position"))
temp=a[n]
a[n]=a[m]
a[m]=temp
print(a)
