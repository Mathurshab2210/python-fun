list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
result=[]

odd=list1[1: :2]
even=list2[0::2]
result.extend(even)
result.extend(odd)
print(result)