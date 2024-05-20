from Video.Video import Video

class Series(Video):
    
    # class attribute
    all = []
    
    def __init__(self, title, duration, launch='2000'):
        super().__init__(title, duration, launch)
        Series.all.append(self)

    def __repr__(self):
        return f"Serie( '{self.title}', '{self.duration}', '{self.duration}')"

