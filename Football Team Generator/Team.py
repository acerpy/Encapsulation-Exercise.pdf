from Class_Player import Player
class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []
        self.new_collection = self.__players
    
    def get_name(self):
        return self.__name
    def get_rating(self):
        return self.__rating
    
    def set_name(self, name):
        self.__name = name
    def set_rating(self, rating):
        self.__rating = rating
    
    def add_player(self, player : Player):
        for plr in self.__players:
            if(player.get_name() == plr.get_name()):
                return f"Player {player.get_name()} has already joined "
        
        self.__players.append(player)
        return f"Player {player.get_name()} joined team {self.__name}"
    
    def remove_player(self, player_name: str):
        for plr in self.__players:
            if(plr.get_name() == player_name):
                self.__players.remove(plr)
                return plr
        return f"Player {player_name} not found"

p1 = Player("Messi", 90, 92, 95, 94, 93)
p2 = Player("Ronaldo", 85, 91, 88, 82, 90)

team = Team("FC Legends", 95)

print(team.add_player(p1))  
print(team.add_player(p1))  
print(team.add_player(p2))  

print(team.remove_player("Messi"))  
print(team.remove_player("Xavi"))   
