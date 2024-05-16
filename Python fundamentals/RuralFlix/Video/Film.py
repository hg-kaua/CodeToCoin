from Video.Video import Video
from time import sleep

class Film(Video):
    
    def __init__(self, title, duration, launch='2000'):
        super().__init__(title, duration, launch)
    
    def play(self):
        print('Starting film...')
        sleep(2)
        print(f'{self.title} has started')
        sleep(1)
        
    def stop(self):
        print('Films cannot be paused')
        
    def advance(self):
        if self.time < self.duration: 
            print('Advance 30 seconds')
            self.time += 30
        else:
            print('The video has come to an end')
    
    def comeBack(self):
        if self.time > 0:
            print('Going back 30 seconds')
            self.time -= 30
        else:
            print('The video is already at the beginning')