import random

rules = {
    "s": "w",  # snake beats water
    "w": "g",  # water beats gun
    "g": "s"   # gun beats snake
}

names = {"s": "Snake", "w": "Water", "g": "Gun"}

computer = random.choice(list(rules.keys()))
you = input("Enter your move (s/w/g): ")

if you not in rules:
    print("Invalid move")
else:
    print(f"You chose {names[you]}")
    print(f"Computer chose {names[computer]}")

    if you == computer:
        print("Draw!")
    elif rules[computer] == you:
        print("Computer wins!")
    else:
        print("You win!")
