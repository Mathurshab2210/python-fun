def peak(arr,n):
    if n==1:
        return 0
    if arr[0]>=arr[1]:
        return 0
    if arr[n-1]>=arr[n-2]:
        return 1
    for i in range(0,n-1):
        if(arr[i]>=arr[i-1] and arr[i] >= arr[i+1]):
            return arr[i]

arr=[1,2,3,4,2]
n=len(arr)
print('peak element is ',peak(arr,n))