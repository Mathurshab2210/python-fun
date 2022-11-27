def length(list):
    if list==[]:
        return 0
    else:
        return 1+ length(list[1:])
    
a=[123,34,'kk',45,6,7,7,8,8]
print(length(a))