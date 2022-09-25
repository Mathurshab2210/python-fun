def eqipt(a,n):
    right=0
    for i in range(n):
        right+=a[i]
    left=0
    for i in range(n):
        right-=a[i]
        if right == left:
            return i+1,a[i]
        left=left+a[i]
    return -1
a=[1,5,8,4,2]
n=len(a)
print(eqipt(a,n))