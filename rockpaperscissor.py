import random
while True: # condition to play indifinitely
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices) # random choice made
    player = None

    while player not in choices: # only rock paper or scissor must be entered, else question will run indifinitely
        player = input("rock, paper, or scissors?: ").lower() # small caps conversion

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

# if player not willing to play, quit and break the loop
    if play_again != "yes":
        break

print("See you!")


#print(computer)