from classes.Player import Player

import random

class Tournament():
    def __init__(self, id, tournament_type, max_rounds):
        self.id = id
        self.players = []
        self.type = tournament_type
        self.max_rounds = max_rounds
        self.round = 1
    
    def getId(self):
        return self.id
    
    def getPlayers(self):
        return self.players

    def getRound(self):
        return self.round
    
    def addPlayer(self, name):
        new_index = len(self.players)

        generating_seed = True
        while generating_seed:
            generating_seed = False
            new_seed = random.randint(0, 100)
            for player in self.players():
                if player.getSeed() == new_seed:
                    generating_seed = True

        new_player = Player(new_index, name, new_seed)
        self.players.append(new_player)
    
    def removePlayer(self, player_name):
        for player in self.players:
            if player.getName() == player_name:
                self.players.pop(player)
    
    def _orderPlayers(self, mode):
        match mode:
            case "score":
                sorting = True
                while sorting:
                    sorting = False
                    for i in range(0, len(self.players) - 1):
                        if self.players[i].getScore() > self.players[i + 1].getScore():
                            temp = self.players[i]
                            self.players[i] = self.players[i + 1]
                            self.players[i + 1] = temp
                            sorting = True
            case "seed":
                sorting = True
                while sorting:
                    sorting = False
                    for i in range(0, len(self.players) - 1):
                        if self.players[i].getSeed() > self.players[i + 1].getSeed():
                            temp = self.players[i]
                            self.players[i] = self.players[i + 1]
                            self.players[i + 1] = temp
                            sorting = True