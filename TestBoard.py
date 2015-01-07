__author__ = 'shiva'

import board
import unittest
import rangeException
import consolegui
import game

class TestBoard(unittest.TestCase):

    def test_SetColumnOK(self):
        brd = board.Board(1, 1)
        brd.setColumn(12)
        self.assertEquals(brd.c, 12)

    def test_SetColumnOdd(self):
        brd = board.Board(1, 1)
        try:
            brd.setColumn(13)
            self.fail("RangeException expected.")
        except rangeException.RangeException:
            pass

    def test_consolegui(self):
        brd = board.Board(12, 6)
        brd.setup()
        brd.begin()
        consolegui.showboard(brd, 0, 0)

    def test_get_score(self):
        brd = board.Board(12, 6)
        brd.setup()
        brd.begin()
        pb, pw = brd.get_score()
        consolegui.showboard(brd, pb, pw)

    def test_put_disc(self):
        brd = board.Board(12, 6)
        brd.setup()
        brd.begin()
        pb, pw = brd.get_score()
        consolegui.showboard(brd, pb, pw)
        lists =  brd.put_disc(2,[5,1])
        self.assertEquals(lists,[(5, 2)])

    def test_put_disc(self):
        brd = board.Board(12, 6)
        brd.setup()
        brd.begin()
        pb, pw = brd.get_score()
        print pb, pw
        consolegui.showboard(brd)
#        lists =  brd.check_disc(2,[5,1])
#        self.assertEquals(lists,[(5, 2)])
        print brd.has_turn(2)
        brd.put_discs(2,[5,1])
        consolegui.showboard(brd)
        pb, pw = brd.get_score()
        print pb,pw

