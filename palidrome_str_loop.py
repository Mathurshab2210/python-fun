s=input("enter a word:").lower()
n=len(s)
for i in range(n):
    if (s[i] != s[n-i-1]):
        print("Not a palindrome")
        break
print("palindrome")
        
    
