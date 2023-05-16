import random
again = "yes"
while again == "yes":
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)
    player = input("Enter Rock, Paper & Scissor: ").lower()
    while player not in choices:
        player = input("Enter Rock, Paper & Scissor: ").lower()

    print("Player: " + player.capitalize())
    print("Computer: " + computer.capitalize())

    if player == computer:
        print("Tie!!!")
    elif player == "rock":
        if computer == "scissor":
            print("You won :)")
        else:
            print("You loss:(")
    elif player == "scissor":
        if computer == "paper":
            print("You won :)")
        else:
            print("You loss:(")
    elif player == "paper":
        if computer == "rock":
            print("You won :)")
        else:
            print("You loss:(")

    again = input("Play again Yes n No:").lower()

print("Good Bye!!")

