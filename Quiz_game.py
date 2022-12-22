print("Computer Quiz")
playing=input("Do you want to play:y/n ")
chk=playing.lower()
if chk !='y':
    quit()

print("Lets Start!!")
s=0
c=0
ans=input("Who was the first person in space? \n")
if ans.lower()=='Yuri Gagarin':
    print("Correct")
    s=s+1
    c=c+1
else:
    print("incorrect\n correct is Yuri Gagarin")
    c=c+1

ans=input("Some who suffer from Alopecia lacks what? \n")
if ans.lower()=='Hair':
    print("Correct")
    s=s+1
    c=c+1
else:
    print("incorrect\n correct is Hair")
    c=c+1


ans=input("What is the chemical symbol of Tungsten?\n")
if ans.lower()=='w':
    print("Correct")
    s=s+1
    c=c+1
else:
    print("incorrect\n correct is W")
    c=c+1


ans=input("What do Ombrophobes have a fear of? \n")
if ans.lower()=='rain':
    print("Correct")
    s=s+1
    c=c+1
else:
    print("incorrect\n correct is Rain")
    c=c+1
    


ans=input("How many Noble Gasses are there?\n")
if ans.lower()=='6':
    print("Correct")
    s=s+1
    c=c+1
else:
    print("incorrect\n correct is 6")
    c=c+1


ans=input("What mineral has the lowest number on the Mohs scale? \n")
if ans.lower()=='talc':
    print("Correct")
    s=s+1
    c=c+1
else:
    print("incorrect\n correct is Talc")
    c=c+1


ans=input("During which war were the concentration camps invented? \n")
if ans.lower()=='boer war':
    print("Correct")
    s=s+1
    c=c+1
else:
    print("incorrect\n correct is Boer war")
    c=c+1


print('Your Score is :',s,'out of :',c) 