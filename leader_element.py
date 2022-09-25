def leader(arr,n):
    for i in range(0,n):
        for j in range(i,n):
            if arr[i]<arr[j]:
                break
        if j==n-1:
            print( arr[i])
        
arr=[1,6,7,5]
n=len(arr)
leader(arr,n)