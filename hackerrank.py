x = int(input())
y = int(input())
z = int(input())
n = int(input())
output = [];
abc = [];
for x in range(x+1):
    for y in range(y+1):
        for z in range(z+1):
            if x+y+z!=n:
                abc=[x,y,z]
                output.append(abc)
print(output);    