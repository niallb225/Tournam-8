class Player:
    def __init__(self, name, seed):
        self.name = name
        self.score = 0
        self.seed = seed

    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
    
    def getSeed(self):
        return self.seed
    
    def setName(self, name):
        self.name = name
    
    def setScore(self, score):
        self.score = score
    
    def setSeed(self, seed):
        self.seed = seed