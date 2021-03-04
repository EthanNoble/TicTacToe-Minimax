from DataStructures import Tree
from Board import Board
import os
from random import randint
import copy
import time

def checkBoardState(board):
    if (Board.isWinningBoard(board, 1) > 0):
        print("O Wins")
        os.system("pause")
        return True
    elif (Board.isWinningBoard(board, -1) > 0):
        print("X Wins")
        os.system("pause")
        return True
    return False

def main():
    print("Generating AI...")
    tree = Tree(9)
    currentBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while (True):
        if (checkBoardState(currentBoard)):
            currentBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            continue
        tree._searchTree([tree._startNode], currentBoard)
        os.system("cls")
        # print("#########")
        # for board in tree._nextBoards:
        #     Board.display(board._board._board)
        #     print("#########")
        if (len(tree._nextBoards) == 0):
            for i in range(len(currentBoard)):
                if (currentBoard[i] == 0):
                    currentBoard[i] = -1
                    break
            Board.display(currentBoard)
            if (checkBoardState(currentBoard)):
                currentBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                continue
            print("It's a Tie")
            os.system("pause")
            currentBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            continue

        nextMoves = []
        min = tree._nextBoards[0]._value
        index = 0
        for i in range(1, len(tree._nextBoards)):
            if (tree._nextBoards[i]._value < min):
                min = tree._nextBoards[i]._value
                index = i
        for i in range(0, len(tree._nextBoards)):
            if (tree._nextBoards[i]._value == min):
                nextMoves.append(tree._nextBoards[i])
        # print(len(nextMoves))
        # print(len(tree._nextBoards))
        currentBoard = copy.deepcopy(nextMoves[randint(0, len(nextMoves) - 1)]._board._board)
        Board.display(currentBoard)
        if (checkBoardState(currentBoard)):
            currentBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            continue
        
        while (True):
            userInput = int(input("> "))
            if (userInput == -1):
                currentBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                break
            else:
                if (userInput > 8 or userInput < -1):
                    os.system("cls")
                    Board.display(currentBoard)
                    exit()
                elif (currentBoard[userInput] == 0):
                    os.system("cls")
                    currentBoard[userInput] = 1
                    Board.display(currentBoard)
                    time.sleep(1)
                    break
        
if (__name__ == "__main__"):
    main()