# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400,300))
running = True
# Initializing Color
color = (255,0,0)
# Variable to keep our game loop running 
running = True
class player(object):
    def __init__(self) -> None:
        self.rectangle = pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
# game loop 
while running: 
    player.rectangle.move(10,0)
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
    
    pygame.display.flip()


