def reverse(string):
    rs=""
    for i in string:
        rs=i+rs
        
    print("Reversed string is ",rs)
    
string=input("Enter string")
reverse(string)