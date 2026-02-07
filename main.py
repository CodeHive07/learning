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
        if (computer == 1 and you == -1) :#2
            print("Computer win !")
        elif (computer == 1 and you == 0) :#1
            print("You win !")
        elif (computer == -1 and you == 1) :#-2
            print("You win !")
        elif (computer == -1 and you == 0) :#-1
            print("Computer win !")
        elif (computer == 0 and you == 1) :#-1
            print("Computer win !")
        elif (computer == 0 and you == -1) :#1
            print("You win !, GOod Job")
            print("Fuck")

    '''
        We can simplify win logic by figuring out pattern : 
        which here is Computer wins when (computer - you) is 2 or -1
        and user wins when (computer - you) is 1 or -2
    '''
