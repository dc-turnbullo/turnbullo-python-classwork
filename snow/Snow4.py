import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF

class Flake:
    def __init__(self,x_pos,y_pos,velocity,size,movement) -> None:
        self.x = x_pos
        self.y = y_pos
        self.vel = velocity
        self.size = size
        self.move = movement

    def fall(self):
        '''
        if self.move & 2 == 0:
            self.x = self.x +1
        else:
            self.x = self.x -1
        '''
        if self.y > size[1]:
            self.y = 0
            self.x = random.randint(0,size[0]-1)
        else:
            self.y = self.y + self.vel
    
    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x,self.y,self.size,self.size))
        
    #endrecord





flake_v = 1

pygame.init()

# Set the width and height of the screen [width, height]
size = (1400, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


rows = 1000
flakes = [None for j in range(rows)]  

  

for flake in range(rows):  
     flakes[flake] = Flake(random.randint(0,size[0]-1),random.randint(0,size[1]-1), random.randint(1,3),random.randint(0,10),random.randint(1,2))
     
#next row       
print(flakes)  



done = False


clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    

    screen.fill(BLACK)
    
    for flake in flakes:
        flake.fall
        flake.draw

    
    pygame.display.flip()

    
    clock.tick(60)


pygame.quit()