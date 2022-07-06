str=input("enetr string: \n")
chck=[item for item in input("Enter substring to check indexing\n").split()]
res={}
for ele in chck:
    if ele in str:
        strt=str.index(ele)
        res[ele]=[strt, strt+len(ele)-1]
        
print(res)
