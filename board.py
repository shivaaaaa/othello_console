
#   By Shiva Mirzae
#   2016.01.07
#   This module represents the Othello-board.


import rangeException
import numpy

__author__ = 'shiva'
EMPTY = 0
WHITE = 1
BLACK = 2


class Board:
    r = 0
    c = 0

    def __init__(self, r, c):
        self.setColumn(c)
        self.setRow(r)

    def setColumn(self, col):
        if 4 < col < 16 and col % 2 == 0 and float.is_integer(col * 1.0):
            self.c = col
        else:
            raise rangeException.RangeException

    def setRow(self, row):
        if 4 < row < 16 and row % 2 == 0 and float.is_integer(row * 1.0):
            self.r = row
        else:
            raise rangeException.RangeException

    def setup(self):
        self.matrix = numpy.zeros((self.r, self.c), dtype=numpy.int)
        return self.matrix

# This function setups the game with placing 4 discs in the start-position.
    def begin(self, reverse=False):
        self.matrix[self.r / 2 - 1][self.c / 2 - 1] = WHITE if not reverse else BLACK
        self.matrix[self.r / 2][self.c / 2 - 1] = BLACK if not reverse else WHITE
        self.matrix[self.r / 2][self.c / 2] = WHITE if not reverse else BLACK
        self.matrix[self.r / 2 - 1][self.c / 2] = BLACK if not reverse else WHITE


# This function counts the number of each white and black discs ( basically the points ) on the board.
    def get_score(self):
        pb = 0
        pw = 0
        for row in self.matrix:
            for i in row:
                if i == 1:
                    pw += 1
                if i == 2:
                    pb += 1
        return pb, pw

    def isonboard(self,row, col):
        return (self.r > row >= 0) and (self.c > col >= 0)

# Checks whether a move can be made or not. If so, a list of the discs which will be flipped after the move is returned.
    def check_disc(self, color, loca):
        if not self.isonboard(loca[0], loca[1]) or self.matrix[loca[0]][loca[1]] != 0:
            return False
        if color == 2:
            opponent = 1
        else:
            opponent = 2
        listdiscs = []
        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]] # Checks all possible direction to score points
        for direct in directions:
            discstoflip = []
            loc = loca[:]
            loc[0] += direct[0]
            loc[1] += direct[1]
            if self.isonboard(loc[0], loc[1]) and self.matrix[loc[0]][loc[1]] == opponent:
                discstoflip.append((loc[0], loc[1]))
                loc[0] += direct[0]
                loc[1] += direct[1]
                while self.isonboard(loc[0], loc[1]) and self.matrix[loc[0]][loc[1]] == opponent:
                    discstoflip.append((loc[0], loc[1]))
                    loc[0] += direct[0]
                    loc[1] += direct[1]
                if not self.isonboard(loc[0], loc[1]):
                    continue
                if not self.matrix[loc[0]][loc[1]] == color:
                    continue
                listdiscs += discstoflip
        if len(listdiscs) == 0:
            return False
        return listdiscs

# Checks if a player can or cannot make a move at all
    def has_turn(self, color):
        for a in range(self.r):
            for b in range(self.c):
                v = self.check_disc(color,[a, b])
                if v != False and len(v) != 0:
                    return True

        return False

    def put_discs(self, color, loc):
        v = self.check_disc(color, loc)
        if v != False:
            self.matrix[loc[0]][loc[1]] = color
            for l in v:
                self.matrix[l[0]][l[1]] = color
        else:
            return False

















