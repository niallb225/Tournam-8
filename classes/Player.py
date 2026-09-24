class Player:
    def __init__(self, index, name, seed):
        self.index = index
        self.name = name
        self.score = 0
        self.seed = seed
    
    def getIndex(self):
        return self.index

    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
    
    def getSeed(self):
        return self.seed
    
    def setIndex(self, index):
        self.index = index
    
    def setName(self, name):
        self.name = name
    
    def setScore(self, score):
        self.score = score
    
    def setSeed(self, seed):
        self.seed = seed