import pygame, sys
from pygame.math import Vector2 as vector
from settings import *

# class for editing the game
class Editor:
    def __init__(self):
        
        # main setup
        # this allows us to draw on the display surface so what the player sees right away
        self.display_surface = pygame.display.get_surface()
        
        # navigation
        self.origin = vector()
        self.pan_active = False
        self.pan_offset = vector()
        
         # support lines
        self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT)) # Copying our entire display surface
        self.support_line_surf.set_colorkey('green')
        self.support_line_surf.set_alpha(30)
        
        
    #input
    def pan_input(self, event):
        #middle mouse button pressed / released
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
            self.pan_active = True
            self.pan_offset = vector(pygame.mouse.get_pos() - self.origin)
            
        if not pygame.mouse.get_pressed()[1]:
            self.pan_active = False
        
        # mouse wheel
        if event.type == pygame.MOUSEWHEEL:
            #checks if we hold the left control on the keyboard
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                self.origin.y -= event.y * 50
            else:
                self.origin.x -= event.y * 50
            
        if self.pan_active:
            self.origin = vector(pygame.mouse.get_pos()) - self.pan_offset
        
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pan_input(event)
    
    #drawing
    def draw_tile_lines(self):
        cols = WINDOW_WIDTH // TILE_SIZE
        rows = WINDOW_HEIGHT // TILE_SIZE
        
        # tuka si pravim nqkva tochka, ot koqto da pochvame da chertaem liniite i tq trqbva
        # da e v purvata kolona nqkude i realno zapochvame da chertaem ot neq, a ne ot chervenata
        # tochka. Purvo sa narisuvani liniite i posle chervenata tochka.
        # realno purvata liniq ni e na tozi x, koito e na offset_vector
        offset_vector = vector(x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE, y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE)
        
        self.support_line_surf.fill('green')
        
        for col in range(cols):
            x = offset_vector.x + col * TILE_SIZE # x that we start to draw every line from
            pygame.draw.line(self.support_line_surf, 'black', (x,0), (x,WINDOW_HEIGHT))
        
        for row in range(rows + 1):
            y = offset_vector.y + row * TILE_SIZE
            pygame.draw.line(self.support_line_surf, 'black', (0, y), (WINDOW_WIDTH, y))
    
        self.display_surface.blit(self.support_line_surf, (0, 0))
    
    def run(self, delta_time):
        self.display_surface.fill('white')
        self.event_loop()
        
        # drawing
        self.draw_tile_lines()
        
        pygame.draw.circle(self.display_surface, 'red', self.origin, 10)