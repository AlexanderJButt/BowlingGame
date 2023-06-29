#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    """BowlingGame Class
    
        this class takes integers(repersenting the number of pins knocked down in a bowl) assigns them to an array
        and then calculates the score based on the rules of bowling"""
    
    def __init__(self):
        self.scoreBoard=[]
        '''Creates scoreBoard array to store the bowls of a player.'''

    def rolls(self,pins):
        self.scoreBoard.append(pins)
        '''Rolls function
        
        Appends bowl(number of pins knocked down in one bowl) to the scoreBoard array.'''

    def score(self):
        '''Score function
        
        calculates score based on the scoreBoard by following the rules of bowling '''
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if frameIndex == 9:
                result += self.lastFrame(rollIndex)
            elif self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=2
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    def isStrike(self, rollIndex):
        '''isStrike function
        
            checks to see if the bowl made was a strike'''
        return self.scoreBoard[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        '''isSpare function
        
            checks to see if the bowls made was a spare'''
        return self.scoreBoard[rollIndex]+ self.scoreBoard[rollIndex+1] == 10  and  self.scoreBoard[rollIndex] != 10

    def strikeScore(self,rollIndex):
        '''strikeScore function
        
            calculates the score when a strike has been bowled'''
        if self.scoreBoard[rollIndex+2] != 10:
            return  10+ self.scoreBoard[rollIndex+2]+ self.scoreBoard[rollIndex+3]
        elif self.scoreBoard[rollIndex+2] + self.scoreBoard[rollIndex+4] == 20:
            return 10+10+10
        else:
            return 10+10+self.scoreBoard[rollIndex+5]
    def spareScore(self,rollIndex):
        '''spearScore function
        
            calculates the score when a spare has been bowled'''
        return  10+ self.scoreBoard[rollIndex+2]

    def frameScore(self, rollIndex):
        '''frameScore function
        
            calculates the score when neither a strike or spear have been bowled'''
        return self.scoreBoard[rollIndex] + self.scoreBoard[rollIndex + 1]
	
    def lastFrame(self,rollIndex):
        if self.scoreBoard[rollIndex] + self.scoreBoard[rollIndex+1] < 10:
            return self.frameScore(rollIndex)
        else:
            return self.scoreBoard[rollIndex] + self.scoreBoard[rollIndex+1] + self.scoreBoard[rollIndex+2]
        
#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS. python -m pydoc -w BowlingGame