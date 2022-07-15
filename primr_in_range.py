for i in range(100,200):
    if all(i%j!=0 for j in range(2,i)):
           print(i)