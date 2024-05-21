from Video.Video import Video

class Series(Video):
    
    # class attribute
    all = []
    
    def __init__(self, title, duration, episodes, seasons, launch='2000'):
        super().__init__(title, duration, launch)
        self.__episodes = episodes
        self.__seasons = seasons
        
        Series.all.append(self)

    
    # implementing decoretes and getters and setters methods
    
    @property
    def seasons(self):
        return self.__seasons
    
    # setters
    @seasons.setter
    def seasons(self, value):
        if value < self.__seasons:
            raise Exception("Impossible to uptade sessons value")
        else:
            self.__seasons = value
            
    @property
    def episodes(self):
        return self.__episodes
    
    # setters
    @episodes.setter
    def episode(self, value):
        if value >= 25:
            raise Exception("Episode value are unavailable") 
        else:
            self.__episodes = value
    
    
    def __repr__(self):
        return f"Serie( '{self.title}', '{self.duration}min', '{self.__episodes}', '{self.__seasons}', '{self.launch}')"

