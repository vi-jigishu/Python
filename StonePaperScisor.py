#A simple stone, paper, scissors game using 'random' module

import random

options=("stone", "paper", "scissors")

playing= True

while playing:       #Its easier to find a boolean variable when a lot of code is in while loop. Otherwise we can just use "while True:" condition and in the end put a break statement using a 'if' statement in the end.
    player= None
    computer= random.choice(options)

    while player not in options:            #To keep check that user inputs a valid option from the module "options"
        player= input("Enter a choice (stone, paper, scissors): ")

    print(f"Player: {player}")       #F strings allows us to use variables and call methods or peroform algebric operations in in a print statement using replacement fields--"{}" 
    print(f"Computer: {computer}")

    if player==computer:
        print("It's a tie!")

    elif player == "stone" and computer == "scissors":
        print("You win!")

    elif player == "paper" and computer == "stone":
        print("You win!")

    elif player == "scissors" and computer == "paper":
        print("You win!")

    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower()=="y":       #".lower()" has been used to lowercase the input by user in case he enters an uppercase input!
        playing = False

print("Thanks for playing!")



