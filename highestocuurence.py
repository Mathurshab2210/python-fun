str=input("enter string")
dict={}
for i in str:
    if i in dict:
        dict[i] +=1
    else:
        dict[i]=1
        
high=sorted(dict.items())
print(high[0])

