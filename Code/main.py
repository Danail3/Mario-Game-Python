import pygame
from settings import *

from editor import Editor

class Main:
    #initializes pygame
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #controls frame rate
        self.clock = pygame.time.Clock()
        self.editor = Editor()
        
        # cursor
        surf = pygame.image.load('Graphics/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0, 0), surf)
        pygame.mouse.set_cursor(cursor)
       
    
    def run(self):
        while True:
            #needed for the game to run smoothly
            delta_time = self.clock.tick() / 1000

                
            self.editor.run(delta_time)
            pygame.display.update()
    
# checking if we are in the main file
if __name__ == '__main__':
    main = Main()
    # inside of this instance we are running the whole game
    main.run() 
        