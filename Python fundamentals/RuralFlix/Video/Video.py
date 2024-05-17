from time import sleep

class Video:
    def __init__(self, title, duration, launch='2000'):
        # Run validation to the received arguments
        assert duration >= 0
        assert launch >= 1900
         
       # Assign to self object  
        self.title = title
        self.duration = duration
        self.launch = launch
        self.time = 0
        
    def play(self):
        print('Starting video...')
        sleep(2)
        print(f'{self.title} has started')
        sleep(1)
    
    def stop(self):
        print('Video pause')
        
    def advance(self):
        if self.time < self.duration: 
            print('Advance 15 seconds')
            self.time += 15
        else:
            print('The video has come to an end')
    
    def comeBack(self):
        if self.time > 0:
            print('Going back 15 seconds')
            self.time -= 15
        else:
            print('The video is already at the beginning')