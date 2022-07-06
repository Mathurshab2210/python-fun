str=input("Enter the string:\n")
char=input("enter the symbol to replace it :\n")
n=int(input("Enter the n value for the replacement:\n"))
out=""
for index,letter in enumerate(str):
    if index%n==0 and index!=0:
        out=out + char
    else:
        out=out+letter
print(out)