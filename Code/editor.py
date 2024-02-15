# import pygame, sys
# from pygame.math import Vector2 as vector
# from settings import *
# from menu import Menu
# # class for editing the game
# class Editor:
#     def __init__(self):
        
#         # main setup
#         # this allows us to draw on the display surface so what the player sees right away
#         self.display_surface = pygame.display.get_surface()
        
#         # navigation
#         self.origin = vector()
#         self.pan_active = False
#         self.pan_offset = vector()
        
#          # support lines
#         self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT)) # Copying our entire display surface
#         self.support_line_surf.set_colorkey('green')
#         self.support_line_surf.set_alpha(30)
        
#         # selection
#         self.selection_index = 2
        
#         # menu
#         self.menu = Menu()
        
#     #input
#     def event_loop(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             self.pan_input(event)
#             self.selection_hotkeys(event)
#             self.menu_click(event)
            
#     def pan_input(self, event):
#         #middle mouse button pressed / released
#         if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
#             self.pan_active = True
#             self.pan_offset = vector(pygame.mouse.get_pos()) - self.origin
            
#         if not pygame.mouse.get_pressed()[1]:
#             self.pan_active = False
        
#         # mouse wheel
#         if event.type == pygame.MOUSEWHEEL:
#             #checks if we hold the left control on the keyboard
#             if pygame.key.get_pressed()[pygame.K_LCTRL]:
#                 self.origin.y -= event.y * 50
#             else:
#                 self.origin.x -= event.y * 50
            
#         if self.pan_active:
#             self.origin = vector(pygame.mouse.get_pos()) - self.pan_offset
        
    
    
#     def selection_hotkeys(self, event):
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 self.selection_index += 1
#             if event.key == pygame.K_LEFT:
#                 self.selection_index -= 1
#         self.selection_index = max(2, min(self.selection_index, 18))
       
#     def menu_click(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN and self.menu.rect.collidepoint(pygame.mouse.get_pos()):
#             self.menu.click(pygame.mouse.get_pos(), pygame.key.get_pressed())
    
#     #drawing
#     def draw_tile_lines(self):
#         cols = WINDOW_WIDTH // TILE_SIZE
#         rows = WINDOW_HEIGHT // TILE_SIZE
        
#         # tuka si pravim nqkva tochka, ot koqto da pochvame da chertaem liniite i tq trqbva
#         # da e v purvata kolona nqkude i realno zapochvame da chertaem ot neq, a ne ot chervenata
#         # tochka. Purvo sa narisuvani liniite i posle chervenata tochka.
#         # realno purvata liniq ni e na tozi x, koito e na offset_vector
#         offset_vector = vector(x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE, y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE)
        
#         self.support_line_surf.fill('green')
        
#         for col in range(cols):
#             x = offset_vector.x + col * TILE_SIZE # x that we start to draw every line from
#             pygame.draw.line(self.support_line_surf, 'black', (x,0), (x,WINDOW_HEIGHT))
        
#         for row in range(rows + 1):
#             y = offset_vector.y + row * TILE_SIZE
#             pygame.draw.line(self.support_line_surf, 'black', (0, y), (WINDOW_WIDTH, y))
    
#         self.display_surface.blit(self.support_line_surf, (0, 0))
    
#     def run(self, delta_time):
        
#         self.event_loop()
        
#         # drawing
#         self.draw_tile_lines()
#         self.display_surface.fill('white')
        
#         pygame.draw.circle(self.display_surface, 'red', self.origin, 10)
#         self.menu.display()
#         print(self.selection_index)

import pygame, sys 
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from settings import *

from menu import Menu

class Editor:
	def __init__(self):
		# main setup 
		self.display_surface = pygame.display.get_surface()

		# navigation
		self.origin = vector()
		self.pan_active = False
		self.pan_offset = vector()

		# support lines 
		self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.support_line_surf.set_colorkey('green')
		self.support_line_surf.set_alpha(30)

		# selection
		self.selection_index = 2

		# menu 
		self.menu = Menu()


	# input
	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			self.pan_input(event)
			self.selection_hotkeys(event)
			self.menu_click(event)

	def pan_input(self, event):

		# middle mouse button pressed / released 
		if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
			self.pan_active = True
			self.pan_offset = vector(mouse_pos()) - self.origin

		if not mouse_buttons()[1]:
			self.pan_active = False

		# mouse wheel 
		if event.type == pygame.MOUSEWHEEL:
			if pygame.key.get_pressed()[pygame.K_LCTRL]:
				self.origin.y -= event.y * 50
			else:
				self.origin.x -= event.y * 50


		# panning update
		if self.pan_active:
			self.origin = vector(mouse_pos()) - self.pan_offset

	def selection_hotkeys(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.selection_index += 1
			if event.key == pygame.K_LEFT:
				self.selection_index -= 1
		self.selection_index = max(2,min(self.selection_index, 18))

	def menu_click(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and self.menu.rect.collidepoint(mouse_pos()):
			self.selection_index = self.menu.click(mouse_pos(), mouse_buttons())

	# drawing 
	def draw_tile_lines(self):
		cols = WINDOW_WIDTH // TILE_SIZE
		rows = WINDOW_HEIGHT// TILE_SIZE

		origin_offset = vector(
			x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
			y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE)

		self.support_line_surf.fill('green')

		for col in range(cols + 1):
			x = origin_offset.x + col * TILE_SIZE
			pygame.draw.line(self.support_line_surf,LINE_COLOR, (x,0), (x,WINDOW_HEIGHT))

		for row in range(rows + 1):
			y = origin_offset.y + row * TILE_SIZE
			pygame.draw.line(self.support_line_surf,LINE_COLOR, (0,y), (WINDOW_WIDTH,y))

		self.display_surface.blit(self.support_line_surf,(0,0))

	def run(self, dt):
		self.event_loop()

		# drawing
		self.display_surface.fill('gray')
		self.draw_tile_lines()
		pygame.draw.circle(self.display_surface, 'red', self.origin, 10)
		self.menu.display(self.selection_index)