def subArraySum(arr, n, s): 
       #Write your code here
       for i in range(0,n):
           currsum=arr[i]
           if currsum == s:
               return i
           else:
                for j in range(i+1,n):
                    currsum=currsum + arr[i]
                    if currsum == s:
                        return i,j


arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
s= 8
 
print(subArraySum(arr, n,s))