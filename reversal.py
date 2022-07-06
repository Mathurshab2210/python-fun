str=input("enter string")
words=str.split()
out=""
for word in words:
    x=word[::-1]
    out=out+" " + x
    
print(out)

    