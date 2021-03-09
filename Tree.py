import BoardData
from Board import Board
import copy
from time import sleep
from random import randint
class NodeTTT:
    _parent = None
    _children = None
    _board = None
    _playerThatMoves = None
    _value = None

    def __init__(self):
        self._children = []
        self._value = 0

class Tree:
    _startNode = None

    def __init__(self, startNode):
        self._startNode = startNode

class LinkedTreeTTT(Tree):
    _numberOfNodes = None
    _childrenPerNode = None
    _isDecreasing = None
    _nextMove = None

    def __init__(self, childrenPerNode, isDecreasing = False):
        super().__init__(NodeTTT())
        self._startNode._board = copy.deepcopy(BoardData.BOARD_EMPTY)
        self._numberOfNodes = 1
        self._childrenPerNode = childrenPerNode
        self._isDecreasing = isDecreasing
        self._generateTree([self._startNode], self._childrenPerNode)

    def _getNextMove(self, nodes, board):
        for node in nodes:
            if (Board.isEqual(node._board, board)):
                #If these are the children of the startNode,
                #make it random as to where the computer plays
                if (len(nodes) == 1):
                    for i in range(0, len(node._children)):
                        node._children[i]._value = -10
                leastValue = node._children[0]._value
                leastValueIndex = 0
                for i in range(0, len(node._children)):
                    # Board.display(node._children[i]._board)
                    # print("-----------", node._children[i]._value)
                    if (node._children[i]._value < leastValue):
                        leastValue = node._children[i]._value
                        leastValueIndex = i
                moveChoice = []
                for i in range(0, len(node._children)):
                    if (node._children[i]._value == leastValue):
                        moveChoice.append(node._children[i]._board)
                self._nextMove = moveChoice[randint(0, len(moveChoice) - 1)]
            self._getNextMove(node._children, board)
                    

    def _generateTree(self, nodes, childrenPerNode, currentPlayer = BoardData.X_PLAYER):
        isFullCount = 0
        for node in nodes:
            if (Board.isFull(node._board)):
                isFullCount += 1
        if (isFullCount == len(nodes)):
            return

        children = []
        for node in nodes:
            for i in range(0, 9):
                if (node._board[i] == BoardData.EMPTY):
                    child = NodeTTT()
                    child._parent = node
                    child._board = copy.deepcopy(node._board)
                    child._playerThatMoves = currentPlayer
                    
                    child._board[i] = currentPlayer

                    node._children.append(child)
                    children.append(child)

                    self._numberOfNodes += 1
        self._generateTree(
            children,
            childrenPerNode if not self._isDecreasing else childrenPerNode - 1,
            BoardData.O_PLAYER if currentPlayer == BoardData.X_PLAYER else BoardData.X_PLAYER
        )

        for child in children:
            boardValue = Board.isWinningBoard(child._board, BoardData.X_PLAYER)
            if (boardValue >= 1):
                child._value -= (boardValue * 10)
                parent = child._parent
                value = (boardValue * 10)
                while (parent != None):
                    parent._value -= value
                    parent = parent._parent
            
            boardValue = Board.isWinningBoard(child._board, BoardData.O_PLAYER)
            if (boardValue >= 1):
                child._value += (boardValue * 10)
                parent = child._parent
                value = 10
                while (parent != None):
                    parent._value += value
                    parent = parent._parent
            
            boardValue = Board.isAlmostWinningBoard(child._board, BoardData.O_PLAYER)
            if (boardValue >= 1):
                child._value += (boardValue * 5)
                parent = child._parent
                value = (boardValue * 5)
                while (parent != None):
                    parent._value += value
                    parent = parent._parent
            
            # boardValue = Board.isAlmostWinningBoard(child._board, BoardData.X_PLAYER)
            # if (boardValue >= 1):
            #     child._value -= (boardValue * 5)
            #     parent = child._parent
            #     value = (boardValue * 5)
            #     while (parent != None):
            #         parent._value -= value
            #         parent = parent._parent
            
            boardValue = Board.containsBlockedMove(child._board, BoardData.O_PLAYER)
            if (boardValue >= 1):
                child._value -= (boardValue * 20)
                parent = child._parent
                value = (boardValue * 20)
                while (parent != None):
                    parent._value -= value
                    parent = parent._parent