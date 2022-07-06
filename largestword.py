str=input("Please enetr list of words:\n")
words=str.split()
flist=[]
for word in words:
    flist.append((len(word),word))#parenthesis to make it a single argument as tuples
    
flist.sort()
print(f" Largest  word among the list is {flist[-1][1]} with lenght {len(flist[-1][1])}")
