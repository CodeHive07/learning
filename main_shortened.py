import random
'''
1 for snake 
-1 for water 
0 for gun
'''
gameDict = {"s" : 1 , "w" : -1 , "g" : 0}
computer = random.choice([1 , -1 , 0])
youstr = input("Enter your move : ")
if(youstr not in gameDict) :
    print("Thats not how u Play Idiot")
else : 
    reversegameDict = {1 : "Snake" , -1 : "Water" , 0 : "Gun"}

    you = gameDict[youstr]

    print(f" You Chose {reversegameDict[you]}\n Computer Chose {reversegameDict[computer]} ")
        

    if (computer == you) :
        print("Draw!")

    else :
        if ((computer - you) == 2 or (computer - you) == -1) :
            print("Computer Wins!")
        elif ((computer - you) == -2 or (computer - you) == 1) :
            print("You Win !")