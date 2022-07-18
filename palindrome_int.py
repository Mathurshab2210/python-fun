n=int(input())
rev=0
tmp=n
while n!=0:
    rev=rev*10 +n%10
    n=n//10
    
if(rev == tmp):
    print("Palindrome")
else:
    print("nhi hai")
