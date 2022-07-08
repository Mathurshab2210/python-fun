my=[1,34,56,43,23]
fl=[]
max=my[0]
for i in range(0,len(my)):
    if(my[i]>max):
        max=my[i]
    else:
        fl.append(my[i])
        
fl.sort()
print(fl)
print(fl[-1])