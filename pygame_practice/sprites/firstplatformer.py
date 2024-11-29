import pygame
import random



pwidth = 10
pheight = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = 0x0000ff
pygame.init()

class player(pygame.sprite.Sprite):
    def __init__(self, colour, height, width) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.yvelo = 0
        self.xvelo = 5
    
    def jump(self):
        self.yvelo += 10
    
    def update(self):
        self.grav()

    def grav(self):
        if self.yvelo > 0:
            self.yvelo -=1
    
    def moveleft(self):
        self.rect.x -= self.xvelo
    
    def moveright(self):
        self.rect.x += self.xvelo
    
class Platform(pygame.sprite.Sprite):
 
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False


p1 = player(RED,pwidth,pheight)


while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    pygame.display.flip()
    clock.tick(60)