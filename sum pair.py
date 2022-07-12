arr=[]
n=int(input("enter the lenght of array:"))
print("enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)
target=int(input("enter the sum value to find the pair:"))
arr.sort()
left=0
right=len(arr)-1
while(left<right):
    if(arr[left]+arr[right] >target):
        right=right-1
    elif(arr[left]+arr[right]<target):
        left=left+1
    elif(arr[left]+arr[right]==target):
        print("pairs are ",arr[left] , "and", arr[right])
        right=right-1
        left=left+1
        