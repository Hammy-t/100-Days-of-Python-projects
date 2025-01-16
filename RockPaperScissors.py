import random

def sign(chosenSign):
    rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")        
    paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

    scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    sign = [rock, paper,scissors]
    if chosenSign==1:
        return sign[0]
    elif chosenSign==2:
        return sign[1]
    else:
        return sign[2]

def compTurn():
    compChoice = random.randint(1,4)
    if compChoice == 1:
        print("Computer chose to ROCK onnnn")
        print(sign(compChoice))
    elif compChoice == 2:
        print("Computer chose to lay flat like a PAPER")
        print(sign(compChoice))
    else:
        print("Computer chose to pull a chucky ...")
        print(sign(compChoice))
    return compChoice
    
def playerTurn():
    r = range(1,4)
    playerChoice = int(input("Player's turn, kindly enter 1 for rock, 2 for paper and 3 for scissors: "))
    if playerChoice in r:
        print(sign(int(playerChoice)))
        return playerChoice
    else:
        playerChoice = input("Invalid input! 1 for rock, 2 paper and 3 for scissors :] ")

def mainGame(bestOf):
    game = bestOf
    compTally = 0
    playerTally=0

    if game == 0:
        if playerTally>compTally:
            print("Game over, PLAYER WINSSS")
        else:
            print("Game over, COMPUTER WINSSS")
        return
    else:
        playerChoice = playerTurn()
        print("Computer's turn: ",end="")
        compChoice = compTurn()
            
        if playerChoice==compChoice:
            print("Its a TIEE, not a scarf")

        else:
            if playerChoice == 1:
                if compChoice==2:
                    print("Computer WINS this round")
                    compTally+=1
                elif compChoice ==3:
                    print("Player WINS this round")
                    playerTally+=1

            elif playerChoice == 2:
                if compChoice==1:
                    print("Player WINS this round")
                    playerTally+=1
                elif compChoice ==3:
                    print("Computer WINS this round")
                    compTally+=1

            else:
                if playerChoice == 3:
                    if compChoice==1:
                        print("Computer WINS this round")
                        compTally+=1
                    elif compChoice ==2:
                        print("Player WINS this round")
                        playerTally+=1
    mainGame(game-1)

def main():
    print("Welcome to ROCK PAPER SCISSORS, enter 1 for ROCK, 2 for PAPER, and 3 for SCISSORS")
    bestOf = int(input("Kindly enter how many times you wish to play: "))
    mainGame(bestOf)

main()