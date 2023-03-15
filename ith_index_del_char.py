mystr="newstring"
new=""
n=int(input("enter char index"))

for i in range(0,len(mystr)):
    if i!=n:
        new= new + mystr[i]

print("deleted char result:", new)

