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

    invalidMove = False
    currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
    while (True):
        os.system("cls")
        if (not invalidMove):
            #Generate the next move based on the current board
            tree._getNextMove([tree._startNode], currentBoard)
            currentBoard = copy.deepcopy(tree._nextMove)
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
        
        userMove = int(input(">> "))
        #Just a bunch of confusing conditionals!
        if (userMove == -1):
            currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
            invalidMove = False
        else:
            if (userMove >= 0 and userMove <= 8):
                if (currentBoard[userMove] == BoardData.EMPTY):
                        currentBoard[userMove] = BoardData.O_PLAYER
                        invalidMove = False
                else:
                    invalidMove = True
            else:
                invalidMove = True

        time.sleep(1)

if __name__ == "__main__":
    main()