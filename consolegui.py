__author__ = 'shiva'
from string import maketrans

def showboard(board ):

    for i in range(board.r):
        for j in range(board.c):
            ch = board.matrix[i][j]
            if ch == 0:
                print '.', ' ',
            elif ch == 2:
                print 'B',' ',
            elif ch == 1:
                print 'W', ' ',
        print
        print
#    print "Blacks points:" + str(pb)
#    print "Whites points:" + str(pw)
