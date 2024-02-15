import sys, pygame
from settings import *

class Main:
    #initializes pygame
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #controls frame rate
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            #needed for the game to run smoothly
            delta_time = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            pygame.display.update()
    
# checking if we are in the main file
if __name__ == '__main__':
    main = Main()
    # inside of this instance we are running the whole game
    main.run() 
        