words=[]
m=int(input("etnter no. of words in list"))
for i in range(0,m):
    x=input()
    words.append(x)
print(len(words))  
    
chr=input("enter word to delete")
n=int(input("enter the position "))
c=0
for i in range(0,len(words)):
    if(words[i] == chr):
        c=c+1
        if(c==n):
            del words[i]
    
            
        
print(words)
        