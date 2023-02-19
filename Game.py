import  random

l= ["rock","scissor","paper"]

while True:
    User = int(input('''
     Start the Game...
     1 Yes
     2 No | Exit
    '''))
    User_Count = 0
    Computer_Count = 0
    if User==1:
        for i in range(1,6):
            userInput = int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userInput ==1:
                userchoice = "rock"
            elif userInput ==2:
                userchoice = "scissor"
            elif userInput ==3:
                userchoice = "paper"
            computer = random.choice(l)
            if userchoice == computer:
                print("UserChoice : ",userchoice)
                print("Computer choice : ",computer)
                print("Match Draw!!")
            elif (userchoice=="rock" and computer =="scissor") or (userchoice=="paper" and computer=="rock") or (userchoice=="scissor" and computer=="paper"):
                print("UserChoice : ", userchoice)
                print("Computer choice : ", computer)
                print("You win!! ")
                User_Count = User_Count+1
            else:
                print("UserChoice : ", userchoice)
                print("Computer choice : ", computer)
                print("Computer win!!")
                Computer_Count = Computer_Count + 1
        if User_Count > Computer_Count:
            print("User Points Counts : ", User_Count)
            print("Computer Points Counts : ", Computer_Count)
            print("You win!! ")
        elif Computer_Count > User_Count:
            print("User Points Counts : ", User_Count)
            print("Computer Points Counts : ", Computer_Count)
            print("Computer win!!")
        else:
            print("User Points Counts : ", User_Count)
            print("Computer Points Counts : ", Computer_Count)
            print("Match Draw!!")

    else:
        print("You have decided not to play!!")
        break


