str=input("enter string")
out=""
i=0
for letter in str:
    if (str.index(letter)==i ):
        out=out+letter
        
    i=i+1
    
    
print(out)