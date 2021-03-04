from Board import Board
import copy
import time
import os
class Node:
    _children = None
    _parent = None
    _value = 0
    _playerThatMoves = None
    _board = None
    _read = False

    def __init__ (self, board):
        self._board = board
        self._children = []
    
    def giveValueToNode(self):
        if (self._playerThatMoves == -1):
            self._value -= (15 * Board.isWinningBoard(self._board._board, 1))
            self._value -= (15 * Board.isWinningBoard(copy.deepcopy(self._board._board), -1))
            self._value -= (2 * Board.isAlmostWinningBoard(copy.deepcopy(self._board._board), -1))
        elif (self._playerThatMoves == 1):
            self._value += (15 * Board.isWinningBoard(self._board._board, -1))
            self._value += (15 * Board.isWinningBoard(copy.deepcopy(self._board._board), 1))
            self._value += (2 * Board.isAlmostWinningBoard(copy.deepcopy(self._board._board), 1))

class Tree:
    _startNode = None
    _childrenPerNode = None
    _totalNodes = 0
    _nextBoards = None
    
    def __init__ (self, childrenPerNode):
        self._startNode = Node(Board([0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
        self._childrenPerNode = childrenPerNode
        self._nextBoards = []
        self._generateTree([self._startNode])
    
    def _searchTree(self, nodes, boardToFind):
        # noChildren = 0
        # for node in nodes:
        #     if (len(node._children) == 0):
        #         noChildren += 1
        # if (noChildren == len(node._children)):
        #     return
        nextTreeLevel = []
        self._nextBoards = []
        for node in nodes:
            for child in node._children:
                nextTreeLevel.append(child)
            if (node._board.isEqual(boardToFind)):
                for i in range(0, len(node._children) - 1):
                    self._nextBoards.append(node._children[i])
                return
        
        self._searchTree(nextTreeLevel, boardToFind)

    def _generateTree(self, nodes, currentPlayer = -1):
        if (self._childrenPerNode == 0):
            return
        if (Board.isFull(self._startNode._board._board)):
            return
        children = []
        found = False
        matchingNode = None
        for node in nodes:
            if (not node._read):
                for i in range(0, 9):
                    if (node._board._board[i] == 0):
                        child = Node(Board(copy.deepcopy(node._board._board), 0))
                        child._parent = node
                        child._playerThatMoves = currentPlayer
                        child._board._board[i] = currentPlayer
                        child.giveValueToNode()
                        node._children.append(child)
                        children.append(child)
                        node._read = True
                        # Board.display(child._board._board)
                        # print("==========", child._value)
                        # time.sleep(1)
                        self._totalNodes += 1
        currentPlayer = -currentPlayer
        
        self._childrenPerNode -= 1
        self._generateTree(children, currentPlayer)