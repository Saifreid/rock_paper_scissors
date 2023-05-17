import random
print("Hello welcome to my Rock Paper Scissors game! ")
targetScore = 0
play = False
playerScore = 0
computerScore = 0
playerInput = ""
while play == False:
    try:
        targetScore = int(input("What score to you want to play to? "))
        if targetScore > 0:
            print("Let's Play!")
            play = True
        else:
            raise TypeError
    except:
        print("Error please enter a valid number greater than 0 ")
while play == True:
    try:
        print("Please enter rock/paper/scissors ")
        playerInput = input().lower()
        if playerInput == "rock" or playerInput == "paper" or playerInput == "scissors":
            computerInput = random.randint(1,3000)%3
            if computerInput == 0:
                print("Computer chose rock!")
            if computerInput == 1:
                print("Computer chose paper!")
            if computerInput == 2:
                print("Computer chose scissors!")
            if playerInput == "rock" and computerInput == 0:
                print("Tie no score change")
            elif playerInput == "rock" and computerInput == 1:
                print("Computer wins the round!")
                computerScore += 1
                if computerScore >= targetScore:
                    print("Computer wins the game!")
                    play = False
            elif playerInput == "rock" and computerInput == 2:
                print("You win the round!")
                playerScore += 1
                if playerScore >= targetScore:
                    print("You win the game!")
                    play = False
            elif playerInput == "paper" and computerInput == 0:
                print("You win the round!")
                playerScore += 1
                if playerScore >= targetScore:
                    print("You win the game!")
                    play = False
            elif playerInput == "paper" and computerInput == 1:
                print("Tie no score change")
            elif playerInput == "paper" and computerInput == 2:
                print("Computer wins the round!")
                computerScore += 1
                if computerScore >= targetScore:
                    print("Computer wins the game!")
                    play = False
            elif playerInput == "scissors" and computerInput == 0:
                print("Computer wins the round!")
                computerScore += 1
                if computerScore >= targetScore:
                    print("Computer wins the game!")
                    play = False
            elif playerInput == "scissors" and computerInput == 1:
                print("You win the round!")
                playerScore += 1
                if playerScore >= targetScore:
                    print("You win the game!")
                    play = False
            else:
                print("Tie no score change")
                
        else:
            raise ValueError
    except:
        print("Please enter valid choice")