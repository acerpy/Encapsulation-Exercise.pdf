class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting
    
    def get_name(self):
        return self.__name
    def get_endurance(self):
        return self.__endurance
    def get_sprint(self):
        return self.__sprint
    def get_dribble(self):
        return self.__dribble
    def get_passing(self):
        return self.__passing
    def get_shooting(self):
        return self.__shooting
    
    def set_name(self, name):
        self.__name = name
    def set_endurance(self, endurance):
        self.__endurance = endurance
    def set_sprint(self, sprint):
        self.__sprint = sprint
    def set_dribble(self, dribble):
        self.__dribble = dribble
    def set_passing(self, passing):
        self.__passing = passing
    def set_shooting(self, shooting):
        self.__shooting = shooting
    
    def __str__(self):
        return f'''Player: {self.__name} 
Endurance: {self.__endurance} 
Sprint: {self.__sprint} 
Dribble: {self.__dribble} 
Passing: {self.__passing} 
Shooting: {self.__shooting}
'''