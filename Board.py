import BoardData
import copy
import os
class Board:
    @staticmethod
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

    @staticmethod
    def isEqual(board1, board2):
        for i in range(0, len(board1)):
            if (board1[i] != board2[i]):
                return False
        return True

    @staticmethod
    def isFull(board):
        fullSpacesCount = 0
        for i in range(0, 9):
            if (board[i] != BoardData.EMPTY):
               fullSpacesCount += 1
        if (fullSpacesCount == 9):
            return True
        else:
            return False
    
    @staticmethod
    def display(board):
        for i in range(0, 9):
            if (i % 3 == 0 and i != 0):
                print('')
            if (board[i] == BoardData.X_PLAYER):
                print('X ', end='')
            elif (board[i] == BoardData.O_PLAYER):
                print('O ', end='')
            else:
                print('- ', end='')
        print('')

    @staticmethod
    def isWinningBoard(board, playerToCheckWin):
        numberOfWinningMoves = 0
        if (board[0] == playerToCheckWin and board[1] == playerToCheckWin and board[2] == playerToCheckWin):
            numberOfWinningMoves += 1
        elif (board[3] == playerToCheckWin and board[4] == playerToCheckWin and board[5] == playerToCheckWin):
            numberOfWinningMoves += 1
        elif (board[6] == playerToCheckWin and board[7] == playerToCheckWin and board[8] == playerToCheckWin):
            numberOfWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[3] == playerToCheckWin and board[6] == playerToCheckWin):
            numberOfWinningMoves += 1
        elif (board[1] == playerToCheckWin and board[4] == playerToCheckWin and board[7] == playerToCheckWin):
            numberOfWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[5] == playerToCheckWin and board[8] == playerToCheckWin):
            numberOfWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[4] == playerToCheckWin and board[8] == playerToCheckWin):
            numberOfWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[4] == playerToCheckWin and board[6] == playerToCheckWin):
            numberOfWinningMoves += 1
        return numberOfWinningMoves

    @staticmethod
    def containsBlockedMove(board, playerToCheckWin):
        numberOfAlmostWinningMoves = 0
        if (board[0] == playerToCheckWin and board[1] == playerToCheckWin and board[2] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[3] == playerToCheckWin and board[4] == playerToCheckWin and board[5] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[6] == playerToCheckWin and board[7] == playerToCheckWin and board[8] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[3] == playerToCheckWin and board[6] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[1] == playerToCheckWin and board[4] == playerToCheckWin and board[7] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[5] == playerToCheckWin and board[8] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[1] == playerToCheckWin and board[2] == playerToCheckWin and board[0] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[4] == playerToCheckWin and board[5] == playerToCheckWin and board[3] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[7] == playerToCheckWin and board[8] == playerToCheckWin and board[6] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[3] == playerToCheckWin and board[6] == playerToCheckWin and board[0] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[4] == playerToCheckWin and board[7] == playerToCheckWin and board[1] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[5] == playerToCheckWin and board[8] == playerToCheckWin and board[2] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[2] == playerToCheckWin and board[1] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[3] == playerToCheckWin and board[5] == playerToCheckWin and board[4] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[6] == playerToCheckWin and board[8] == playerToCheckWin and board[7] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[6] == playerToCheckWin and board[3] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[1] == playerToCheckWin and board[7] == playerToCheckWin and board[4] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[8] == playerToCheckWin and board[5] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[4] == playerToCheckWin and board[8] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[4] == playerToCheckWin and board[8] == playerToCheckWin and board[0] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[8] == playerToCheckWin and board[4] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[4] == playerToCheckWin and board[6] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[4] == playerToCheckWin and board[6] == playerToCheckWin and board[2] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[6] == playerToCheckWin and board[4] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        return numberOfAlmostWinningMoves

    @staticmethod
    def isAlmostWinningBoard(board, playerToCheckWin):
        numberOfAlmostWinningMoves = 0
        if (board[0] == playerToCheckWin and board[1] == playerToCheckWin and not board[2] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[3] == playerToCheckWin and board[4] == playerToCheckWin and not board[5] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[6] == playerToCheckWin and board[7] == playerToCheckWin and not board[8] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[3] == playerToCheckWin and not board[6] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[1] == playerToCheckWin and board[4] == playerToCheckWin and not board[7] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[5] == playerToCheckWin and not board[8] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[1] == playerToCheckWin and board[2] == playerToCheckWin and not board[0] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[4] == playerToCheckWin and board[5] == playerToCheckWin and not board[3] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[7] == playerToCheckWin and board[8] == playerToCheckWin and not board[6] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[3] == playerToCheckWin and board[6] == playerToCheckWin and not board[0] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[4] == playerToCheckWin and board[7] == playerToCheckWin and not board[1] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[5] == playerToCheckWin and board[8] == playerToCheckWin and not board[2] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[2] == playerToCheckWin and not board[1] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[3] == playerToCheckWin and board[5] == playerToCheckWin and not board[4] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[6] == playerToCheckWin and board[8] == playerToCheckWin and not board[7] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[0] == playerToCheckWin and board[6] == playerToCheckWin and not board[3] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[1] == playerToCheckWin and board[7] == playerToCheckWin and not board[4] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        elif (board[2] == playerToCheckWin and board[8] == playerToCheckWin and not board[5] == -playerToCheckWin):
            numberOfAlmostWinningMoves += 1
        return numberOfAlmostWinningMoves