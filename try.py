can1=input("Enter candidate name:\n")
can2=input("Enter candidate name:\n")

can1_vote=0
can2_vote=0
voters_id=[101,102,103,104]
no_voters=len(voters_id)
voted=[]
  
while True:
    if voters_id==[]:
        print("Voting is over!!")
        
        if can1_vote > can2_vote:
            print(f"{can1} won with votes {can1_vote}")
        elif can1_vote < can2_vote:
             print(f"{can2} won with votes {can2_vote}")
        elif can1_vote == can2_vote:
            print("Tied !!")
        break
    
    else:
        voter=int(input("Enter your id"))
        if voter in voted :
            print("You alreday voted")
        else:
           if voter in voters_id:
                print(f'1.{can1} \n 2.{can2}')
                choice=int(input('enter your chouce:'))
                if choice == 1:
                    can1_vote +=1
                elif choice == 2:
                    can2_vote +=1
                
                voters_id.remove(voter)
                voted.append(voter)
           else:
              print("you can not vote!!")
        
        
        
             
             
             
             
           
             