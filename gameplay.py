
#   By Shiva Mirzae
#   2016.01.07


import board
import unittest
import rangeException
import consolegui
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# Introduction
print
print "Welcome to Reversi aka Othello "
print
print "***"
print
print "Please enter the number of rows of the Othello-board, which should be between 4 and 16."
r = raw_input()
while (not is_number(r)) or (not 4 < r < 16) or (not r % 2 == 0) or (not float.is_integer(r)):
    while not is_number(r):
        print "Please enter a number."
        r = raw_input()
    r = float(r)
    while is_number(r) and (float(r) >= 16 or 4 >= float(r)):
        r = float(r)
        print "Please enter a number between 4 and 16."
        r = raw_input()
    while is_number(r) and ((float.is_integer(float(r))) == False):
        r = float(r)
        print "Please enter an integer"
        r = raw_input()
    while is_number(r) and ((float(r) % 2 == 0) == False):
        r = float(r)
        print "Please enter an even number"
        r = raw_input()

r = int(r)
print "Please enter now the desired number of columns, an even integer between 4 and 16."

c = raw_input()
while (not is_number(c)) or (not 4 < c < 16) or (not c % 2 == 0) or (not float.is_integer(c)):
    while not is_number(c):
        print "Please enter a number."
        c = raw_input()
    c = float(c)
    while is_number(c) and (float(c) >= 16 or 4 >= float(c)):
        c = float(c)
        print "Please enter a number between 4 and 16."
        c = raw_input()
    while is_number(c) and ((float.is_integer(float(c))) == False):
        c = float(c)
        print "Please enter an integer"
        c = raw_input()
    while is_number(c) and ((float(c) % 2 == 0) == False):
        c = float(c)
        print "Please enter an even number"
        c = raw_input()
c = int(c)
print "Which of the players will move first? Black or white?"
p = raw_input().upper()
while not (p == "BLACK" or p == "WHITE" ):
        print "Your answer was not accurate/ you made a typo. Please enter your answer again."
        p = raw_input().upper()
if p == "BLACK":
    p = 2
    o = 1
elif p == "WHITE":
    p = 1
    o = 2

print "According to the rules, the game begins with four discs on the board: two white and two black, arranged on the four center cells of the grid,"
print  "with the two white discs separated diagonally and the two black discs separated diagonally."
print "Traditionally, a white disc will be in the bottom-right position of these four center cells. But you can chose whether you want a black disc there instead or not."
print "Do you want to place a black disc in the bottom-right position?"

re = raw_input().upper()
while not (re == "YES" or re == "NO" ):
        print "Your answer was not accurate/ you made a typo. Please enter your answer again."
        re = raw_input().upper()

if re == "YES":
    re = True
elif re == "NO":
    re = False

print "What does it mean to win the game? There are two choices:"
print "1 - The player with the most discs on the board at the end of the game is the winner."
print "2 - The player with the fewest discs on the board at the end of the game is the winner, which makes for an interesting and different flavor of the game. 1 or 2?"
win = raw_input().upper()
while not (win == "1" or win == "ONE" or win == "2" or win == "TWO"):
        print "Your answer was not accurate/ you made a typo. Please enter your answer again."
        win = raw_input().upper()

if win == "ONE" or win == "1":
    win = 1
elif win == "TWO" or win == "2":
    win = 2
print
print "Thank you for the answers. Enjoy playing..!!"
brd = board.Board(r, c)

brd.setup()
brd.begin(re)

# Start of actual game

co = 0
while brd.has_turn(2) or brd.has_turn(1):
    print
    print "***"
    print
    c += 1
    if c % 2 != 0:
        turn = p
    else:
        turn = o
    consolegui.showboard(brd)
    pb, pw = brd.get_score()
    print "Black's points:" + str(pb)
    print "White's points:" + str(pw)
    if brd.has_turn(turn):
        print ("Black" if turn == 2 else "White") + " has turn."
    else:
        if turn == p:
            turn = o
        else:
            turn = p
        print ("Black" if turn == 2 else "White") + " has turn."
        c += 1
    print "Where do you want to put a disc? Enter first the row-number (from top to bottom, beginning from 0) and then the column-number (from left to right, beginning with 0 as well.)"
    loc1 = raw_input()
    loc2 = raw_input()
    while not is_number(loc1) or not is_number(loc2) or not 0 <= int(loc1) < r or not float.is_integer(float(loc1)) or not 0 <= int(loc2) < c or not float.is_integer(float(loc2)) or not brd.check_disc(turn,[int(loc1), int(loc2)]):
        print "Your move is invalid. Please try again."
        loc1 = raw_input()
        loc2 = raw_input()
    brd.put_discs(turn, [int(loc1), int(loc2)])
print
print "***"
print
consolegui.showboard(brd)
pb, pw = brd.get_score()
pb, pw = str(pb), str(pw)

if win == 1:
    if int(pb) > int(pw):
        print "Black has won!!! Black's points: " + pb + " White's points:" + pw
    elif int(pw) > int(pb):
        print "White has won!!! White's points: " + pw + " Black's points:" + pb
    else:
        "Equal points!! Draw..!! Both have scored " + pw + " points in this round."
else:
    if int(pb) < int(pw):
        print "Black has won!!! Black's points: " + pb + " White's points:" + pw
    elif int(pw) < int(pb):
        print "White has won!!! White's points: " + pw + " Black's points:" + pb
    else:
        "Equal points!! Draw..!! Both have scored " + pw + " points in this round."

print "Thanks for playing!"
print
print "***"
print
