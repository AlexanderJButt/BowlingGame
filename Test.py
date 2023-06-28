#File 1 (Test.py)

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score()==0
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testOneSpare(self):
        self.game.rolls(1)
        self.game.rolls(9)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        self.rollStrikes(1)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testOneStrikeAndOneSpear(self):
        self.rollStrikes(1)
        self.game.rolls(9)
        self.game.rolls(1)
        self.rollMany(0,16)
        assert  self.game.score()==30
    def testStrikeMissStrike(self):
        self.rollStrikes(1)
        self.game.rolls(0)
        self.game.rolls(0)
        self.rollStrikes(1)
        self.rollMany(0,16)
        assert  self.game.score()==20
    def testThreeStrikesAtEnd(self):
        self.rollMany(0,18)
        self.rollStrikes(3)
        assert  self.game.score()==30
    def testPerfectGame(self):
        self.rollStrikes(10)
        self.game.rolls(10)
        self.game.rolls(10)
        assert self.game.score()==300
    def testSpareGame(self):
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.rolls(pins)
    def rollStrikes(self,rolls):
        for i in range(rolls):
            self.game.rolls(10)
            self.game.rolls(0)