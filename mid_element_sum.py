def findMidSum(ar1, ar2, n):
    ar1=list(ar1)
    ar2=list(ar2)
    ar3=[]
    ar3=ar1+ar2
    ar3.sort()
    x=len(ar3)
    n1=x//2
    n2=n1+1
    sum_mid=ar3[n1]+ar3[n2]
        # code here

    print(sum_mid)
            
n= 5
ar1= {1, 12, 15, 26, 38}
ar2= {2, 13, 17, 30, 45}
findMidSum(ar1, ar2, n)