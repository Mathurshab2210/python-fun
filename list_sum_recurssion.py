def sum_list(a):
    if len(a)==0:
        return 0
    else:
        return a[0]+sum_list(a[1:])




a=[1,2,3,4,55,6,7]
print(sum_list(a))