#BellP5
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose:Provide the user with a simple game, with result tracking.

#Handle Imports
from random import randrange    #random number generation is necessary for this script
from os import system

#Initialize a list to store results of each game
resultIndex         =           ["Win","Loss","Tie"] #unused - reference only
results             =           [   0,      0,    0]
win = 0
#Start a game of Rock Paper Scissors (This will be a loop)
while True:
    #initialize our local variables
    rock = 0
    paper = 1
    scissors = 2
    
    #Select a random number, 0-2, assigned to Rock, Paper, or Scissors.
    computerChoice = randrange(2)
    if computerChoice == rock:
        computerChoice = str("Rock")
    elif computerChoice == paper:
        computerChoice = str("Paper")
    elif computerChoice == scissors:
        computerChoice = str("Scissors")
    #Ask the user for their selection (rock paper or scissors)
    playerChoice = str(input("Type 'Rock', 'Paper', or 'Scissors'  : ")).title()
    #Compare the selection to our previously selected number to evaluate for the winner
    if computerChoice == playerChoice: #Define logic for Tie game, quite simple, just a basic comparison
        print("Tie Game!")
        results[2] += 1
        win = 'Tie'
    else: #Define logic for a won or lost game, keep it simple.
        while computerChoice == "Rock":
            if playerChoice == "Paper":
                win = "Player"
                break
            else:
                win = "CPU"
                break
        while computerChoice == "Paper":
            if playerChoice == "Scissors":
                win = "Player"
                break
            else:
                win = "CPU"
                break
        while computerChoice == "Scissors":
            if playerChoice == "Rock":
                win = "Player"
                break
            else:
                win = "CPU"
                break
        if win == "Player": #If the player won, increase the win index by 1
            results[0] +=1
        elif win == "CPU": #If the player lost, increase the loss index by 1.
            results[1] +=1

    #Report back to user each selection, the winner, how many rounds have been played this session, and a win/loss/tie total.
    system("clear") #clear the screen first to keep output clean. Nobody likes a dirty console.
    print(f"The computer chose {computerChoice}.")
    print(f"You chose {playerChoice}.")
    if win == "Player":
        print("You Won!!")
    elif win == "CPU":
        print("CPU Won!!")
    elif win == 'Tie':
        print("Tie Game!!")
    
    rounds = sum(results[:])
    
    print(f'''
        Player Wins:       Computer Wins:      Tie Games:      
            {results[0]}                    {results[1]}                     {results[2]}
        ''')
    print(f"You have played {rounds} rounds.")


    #Ask the user if they'd like to play again, if not, display an exit message and gracefully exit.
    newGame = str(input("Would you like to play again? (Y/N)  : ")).lower()
    if newGame != 'y':
        break
    


'''Notes regarding this project:

I've known python 2.7.x for years, I never mastered it, just enough to do some basic automatation of tasks for my home life. Last year I began learning
Rust. Big fan of Rust. In the textbook I was referencing for Rust, there was a project included for making a simple guessing game.
Have the computer randomly select a number between 1-100 and compare it to the user's guess.

Underneath the wrapper of being a "Rock Paper Scissors" game instead of a simple guessing game, this is the same thing!

There is a little bit more logic to handle the rules of Rock Paper Scissors, so this is nice for learning conditionals but otherwise it's basically the same concept.
It's just neat to see how a simple number guessing game can be extended into Rock Paper Scissors. It makes me think about all the 
complicated games I've played over the years and wonder "How many of these started as number guessing games?"

After all, anything is a game engine if you can write a game with it.

'''
#bonus round: dump the results of each game to a CSV to maintain persistence
#This will be done in a separate document