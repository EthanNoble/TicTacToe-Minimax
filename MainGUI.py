import pygame
from GameObjects import GameObject
import copy
import sys

from Tree import LinkedTreeTTT
from Board import Board
import BoardData

def main():
    pygame.init()

    tree = LinkedTreeTTT(9, True)

    pygame.display.set_caption("Tic-Tac-Toe!")
    screen = pygame.display.set_mode((450, 500))
    screen.fill([180, 180, 180])

    HOVERED_TRANSPARENCY = 75

    X_IMAGE_PATH = "./images/X.png"
    X_WIN_IMAGE_PATH = "./images/XWIN.png"
    O_IMAGE_PATH = "./images/O.png"
    O_WIN_IMAGE_PATH = "./images/OWIN.png"
    EMPTY_IMAGE_PATH = "./images/EMPTY.png"
    GRID1_IMAGE_PATH = "./images/GRID1.png"
    GRID2_IMAGE_PATH = "./images/GRID2.png"

    X_IMAGE = pygame.image.load(X_IMAGE_PATH).convert_alpha()
    X_IMAGE = pygame.transform.scale(X_IMAGE, (150, 150))
    X_IMAGE_WIN = pygame.image.load(X_WIN_IMAGE_PATH).convert_alpha()
    X_IMAGE_WIN = pygame.transform.scale(X_IMAGE_WIN, (150, 150))
    O_IMAGE = pygame.image.load(O_IMAGE_PATH).convert_alpha()
    O_IMAGE = pygame.transform.scale(O_IMAGE, (150, 150))
    O_IMAGE_WIN = pygame.image.load(O_WIN_IMAGE_PATH).convert_alpha()
    O_IMAGE_WIN = pygame.transform.scale(O_IMAGE_WIN, (150, 150))
    EMPTY_IMAGE = pygame.image.load(EMPTY_IMAGE_PATH).convert_alpha()
    EMPTY_IMAGE = pygame.transform.scale(EMPTY_IMAGE, (150, 150))
    GRID1_IMAGE = pygame.image.load(GRID1_IMAGE_PATH).convert()
    GRID1_IMAGE = pygame.transform.scale(GRID1_IMAGE, (150, 150))
    GRID2_IMAGE = pygame.image.load(GRID2_IMAGE_PATH).convert()
    GRID2_IMAGE = pygame.transform.scale(GRID2_IMAGE, (150, 150))
    X_BUTTON_IMAGE = pygame.image.load(X_IMAGE_PATH).convert_alpha()
    X_BUTTON_IMAGE = pygame.transform.scale(X_BUTTON_IMAGE, (50, 50))
    O_BUTTON_IMAGE = pygame.image.load(O_IMAGE_PATH).convert_alpha()
    O_BUTTON_IMAGE = pygame.transform.scale(O_BUTTON_IMAGE, (50, 50))

    buttons = []

    buttons.append(GameObject(X_BUTTON_IMAGE, 50, 50, 0, 450))
    buttons.append(GameObject(O_BUTTON_IMAGE, 50, 50, 50, 450))

    rect1 = buttons[0]._image.get_rect()
    rect1.topleft = (buttons[0]._xPos, buttons[0]._yPos)
    buttons[0]._rect = rect1
    rect2 = buttons[1]._image.get_rect()
    rect2.topleft = (buttons[1]._xPos, buttons[1]._yPos)
    buttons[1]._rect = rect2

    screen.blit(buttons[0]._image, (buttons[0]._xPos, buttons[0]._yPos))
    screen.blit(buttons[1]._image, (buttons[1]._xPos, buttons[1]._yPos))

    #Set each piece as an empty tile with a
    #collision rect (to check for a mouse click)
    pieces = []
    x = 0
    y = 0
    for i in range(0, 9):
        if (i != 0 and i % 3 == 0):
            x = 0
            y += 150
        
        if (i % 2 == 0):
            screen.blit(GRID1_IMAGE, (x, y))

        obj = GameObject(EMPTY_IMAGE, 150, 150, x, y)
        rect = obj._image.get_rect()
        rect.topleft = (x, y)
        obj._rect = rect

        pieces.append(obj)

        x += 150

    currentPlayer = BoardData.O_PLAYER
    playerMoved = True if currentPlayer == BoardData.O_PLAYER else False
    currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
    while (True):
        ###### EVENTS ######
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                #Check for a clicked mouse and find the piece
                #the mouse clicked on
                firstEventFound = False
                
                x, y = event.pos

                clickedObject = None
                for p in pieces:
                    if (p._rect.collidepoint(x, y)):
                        clickedObject = p
                        firstEventFound = True
                        break
                
                #Find the clicked piece in the pieces list
                #and update the currentBoard list with the
                #currentPlayer
                for i in range(0, len(pieces)):
                    if (pieces[i]._image == EMPTY_IMAGE and pieces[i] == clickedObject):
                        currentBoard[i] = currentPlayer
                        playerMoved = True
                        break
            
                #Check if a change player button has been clicked
                if (not firstEventFound):
                    clickedObject = None
                    for b in buttons:
                        if (b._rect.collidepoint(x, y)):
                            clickedObject = b
                            if (clickedObject._image == X_BUTTON_IMAGE):
                                currentPlayer = BoardData.X_PLAYER

                                currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
                                for i in range(0, len(pieces)):
                                    pieces[i]._image = GRID1_IMAGE if i % 2 == 0 else GRID2_IMAGE
                                    screen.blit(pieces[i]._image, (pieces[i]._xPos, pieces[i]._yPos))

                                playerMoved = False
                            elif (clickedObject._image == O_BUTTON_IMAGE):
                                currentPlayer = BoardData.O_PLAYER

                                currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
                                for i in range(0, len(pieces)):
                                    pieces[i]._image = GRID1_IMAGE if i % 2 == 0 else GRID2_IMAGE
                                    screen.blit(pieces[i]._image, (pieces[i]._xPos, pieces[i]._yPos))
                                    
                                playerMoved = True

        #If the mouse is hovering over an empty piece,
        #show a piece
        x, y = pygame.mouse.get_pos()
        hoveredObject = None
        for i in range(0, len(pieces)):
            if (pieces[i]._image == EMPTY_IMAGE or pieces[i]._isHovered):
                if (not pieces[i]._rect.collidepoint(x, y)):
                    pieces[i]._isHovered = False
                if (not pieces[i]._isHovered):
                    if (pieces[i]._rect.collidepoint(x, y)):
                        pieces[i]._image = X_IMAGE.copy() if currentPlayer == BoardData.X_PLAYER else O_IMAGE.copy()
                        pieces[i]._image.set_alpha(HOVERED_TRANSPARENCY)
                        screen.blit(pieces[i]._image, (pieces[i]._xPos, pieces[i]._yPos))
                        pieces[i]._isHovered = True
                    else:
                        pieces[i]._image = GRID1_IMAGE if i % 2 == 0 else GRID2_IMAGE
                        screen.blit(pieces[i]._image, (pieces[i]._xPos, pieces[i]._yPos))
                        pieces[i]._isHovered = False
        
        ###### END OF EVENTS ######
        
        #Keep the pieces updated based on the currentBoard list
        for i in range(0, len(pieces)):
            if (currentBoard[i] == BoardData.X_PLAYER):
                pieces[i]._image = X_IMAGE
                screen.blit(pieces[i]._image, (pieces[i]._xPos, pieces[i]._yPos))
            elif (currentBoard[i] == BoardData.O_PLAYER):
                pieces[i]._image = O_IMAGE
                screen.blit(pieces[i]._image, (pieces[i]._xPos, pieces[i]._yPos))
            elif (currentBoard[i] == BoardData.EMPTY):
                pieces[i]._image = EMPTY_IMAGE
                screen.blit(pieces[i]._image, (pieces[i]._xPos, pieces[i]._yPos))
        
        winningPieces = Board.isWinningBoardGUIDisplay(currentBoard, BoardData.X_PLAYER)
        if (winningPieces[0] != -1):
            pieces[winningPieces[0]]._image = X_IMAGE_WIN
            pieces[winningPieces[1]]._image = X_IMAGE_WIN
            pieces[winningPieces[2]]._image = X_IMAGE_WIN
            screen.blit(pieces[winningPieces[0]]._image, (pieces[winningPieces[0]]._xPos, pieces[winningPieces[0]]._yPos))
            screen.blit(pieces[winningPieces[1]]._image, (pieces[winningPieces[1]]._xPos, pieces[winningPieces[1]]._yPos))
            screen.blit(pieces[winningPieces[2]]._image, (pieces[winningPieces[2]]._xPos, pieces[winningPieces[2]]._yPos))
            playerMoved = True

            currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
            pygame.display.update()
            pygame.time.delay(2000)
        winningPieces = Board.isWinningBoardGUIDisplay(currentBoard, BoardData.O_PLAYER)
        if (winningPieces[0] != -1):
            pieces[winningPieces[0]]._image = O_IMAGE_WIN
            pieces[winningPieces[1]]._image = O_IMAGE_WIN
            pieces[winningPieces[2]]._image = O_IMAGE_WIN
            screen.blit(pieces[winningPieces[0]]._image, (pieces[winningPieces[0]]._xPos, pieces[winningPieces[0]]._yPos))
            screen.blit(pieces[winningPieces[1]]._image, (pieces[winningPieces[1]]._xPos, pieces[winningPieces[1]]._yPos))
            screen.blit(pieces[winningPieces[2]]._image, (pieces[winningPieces[2]]._xPos, pieces[winningPieces[2]]._yPos))
            playerMoved = False

            currentBoard = copy.deepcopy(BoardData.BOARD_EMPTY)
            pygame.display.update()
            pygame.time.delay(2000)

        #Checks if the player has made a move. If so,
        #update the board with the computer's move
        if (playerMoved and not Board.isFull(currentBoard)):
            tree._getNextMove([tree._startNode], currentBoard, currentPlayer)
            currentBoard = copy.deepcopy(tree._nextMove)
            playerMoved = False

        pygame.display.update()

if __name__ == "__main__":
    main()