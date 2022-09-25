def mulsubarr(arr,n):
    result=arr[0]
    for i in range(0,n):
        mul=arr[i]
        for j in range(i+1,n):
            result=max(result,mul)
            mul=mul*arr[j]
        result=max(result,mul)
    return result,mul
arr=[1,5,7,8,12,6,2]
n=len(arr)
print(mulsubarr(arr,n))
