str=input("Enter the sentence:\n")
s1=str.lower()
count=0
vow=["a","e","i","o","u"]
flist=[]
for char in str:
    if char in vow:
        count=count+1
        flist.append(char)
        
filter=[]
for ele in flist:
    if ele not in filter:
        filter.append(ele)
        
dict={}

for chr in flist:
    if chr in dict:
        dict[chr] +=1
    else:
        dict[chr]=1
        
print("count of vow in sentence:",count)
print("list of vowels in the sentece",filter)
print("frequency of vowel in sentence:",dict)

