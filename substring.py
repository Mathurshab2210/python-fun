str=input("Enter the string")
if len(str)<2:
    print("Not enough size")
else:
    s1=slice(0,2)
    s2=slice(len(str)-2 , len(str))
    
print(str[s1] + str[s2])
