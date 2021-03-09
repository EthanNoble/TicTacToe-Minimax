from Tree import LinkedTreeTTT
import BoardData
from Board import Board
import copy
import os
import time

def main():
    os.system("cls")
    print("Generating Computer's Moves...")
    tree = LinkedTreeTTT(9, True)

    while (True):
        while (True):
            player = None
            os.system("cls")
            print("What would you like to do... play X or O?")
            playerChoice = input(">> ")
            if (str.lower(playerChoice) == 'x'):
                player = BoardData.X_PLAYER
                break
            elif (str.lower(playerChoice) == 'o'):
                player = BoardData.O_PLAYER
                break
        
        turns = 0
        invalidMove = False
        currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
        while (True):
            os.system("cls")

            if (turns == 0 and player != BoardData.O_PLAYER):
                time.sleep(1)
                Board.display(currentBoard)

            #Execute this if the player is playing O
            if (player == BoardData.O_PLAYER and not invalidMove):
                #Generate the next move based on the current board
                tree._getNextMove([tree._startNode], currentBoard, player)
                currentBoard = copy.deepcopy(tree._nextMove)
            
            os.system("cls")
            Board.display(currentBoard)

            #Check if X or O has won
            if (Board.checkBoardState(currentBoard)):
                currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
                continue
            #If X or O has not won but the board is full, tie
            elif (Board.isFull(currentBoard)):
                currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
                print("It's a Tie")
                os.system("pause")
                continue
        
            userMove = int(input("(-2 to change player)\n>> "))
            #Just a bunch of confusing conditionals!
            if (userMove == -2):
                invalidMove = False
                break
            else:
                if (userMove >= 0 and userMove <= 8):
                    if (currentBoard[userMove] == BoardData.EMPTY):
                        currentBoard[userMove] = player
                        invalidMove = False
                    else:
                        invalidMove = True
                else:
                    invalidMove = True
            
            os.system("cls")
            Board.display(currentBoard)
            time.sleep(1)
        
            #Execute this if the player is playing X
            if (not Board.isFull(currentBoard) and player == BoardData.X_PLAYER and not invalidMove):
                #Generate the next move based on the current board
                tree._getNextMove([tree._startNode], currentBoard, player)
                currentBoard = copy.deepcopy(tree._nextMove)
            
            turns += 1

if __name__ == "__main__":
    main()