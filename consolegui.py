__author__ = 'shiva'
from string import maketrans
from colorama import init
init()
from colorama import Fore, Back, Style
def showboard(board ):
    for a in range(board.c ):
        print " ", a,
    print
    cr = -1
    for i in range(board.r):
        cr += 1
        print cr,
        for j in range(board.c):
            ch = board.matrix[i][j]
            if ch == 0:
                print '.', ' ',
            elif ch == 2:
                print Fore.RED + 'B' + Fore.RESET,' ',
#                print Fore.RESET + Back.RESET + Style.RESET_ALL,
            elif ch == 1:
                print Fore.BLUE  + 'W'  + Fore.RESET, ' ',
#                print Fore.RESET + Back.RESET + Style.RESET_ALL,
        print