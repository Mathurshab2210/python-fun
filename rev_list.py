a=[1,2,3,4,5,"io",6]
j=1
rev=[]
for i in a:
    rev.append(a[len(a)-j])
    j=j+1
print(rev)