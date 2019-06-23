from random import randint
def selection():
    print("Enter 1 for STONE")
    print("Enter 2 for PAPER")
    print("Enter 3 for SCISSOR")



hn=0
pn=0
print("Welcome to STONE|PAPER|SCISSOR")
print("Enter 1 to start")
c=int(input())
if(c==1):
    valid=True
    while(True):
        selection()

        human=int(input("Enter the number from the choices given"))
        if human==1:
            print("I choose STONE")
        elif human==2:
            print("I Choose PAPER")
        elif human==3:
            print("I choose SCISSOR")
        else:
            print("Choose between 1 2 3. as its a foul the opponent gets a point")

        pc=randint(1,3)
        print(pc)
        

        if((human==1 and pc==1) or (human==2 and pc==2) or (human==3 and pc==3)):
            print("draw")
            print("------------------------------SCORES------------------------------")
            print("User:",hn)
            print("Computer:",pn)
            print("------------------------------------------------------------------")
        elif((human==1 and pc==3) or (human==2 and pc==1) or (human==3 or pc==2)):
            print("Yeah I won")
            hn=hn+1
            print("------------------------------SCORES------------------------------")
            print("User:",hn)
            print("Computer:",pn)
            print("------------------------------------------------------------------")
        else:
            print("The PC won")
            pn=pn+1
            print("------------------------------SCORES------------------------------")
            print("User:",hn)
            print("Computer:",pn)
            print("------------------------------------------------------------------")
        if(pn==5 or hn==5):
            valid=False
            break
        
    if(hn==5):
        print("You won the match,See you next time")
    elif(pn==5):
        print("The pc won the match,See you next time")
    


else:
    print("See you next time")
    

     

    
    
