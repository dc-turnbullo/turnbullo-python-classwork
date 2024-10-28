import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF
class bot:
    def __init__(self,x_pos,y_pos,velocity,size) -> None:
        self.x = x_pos
        self.y = y_pos
        self.vel = velocity
        self.size = size
    #endrecord





xcoord = 0
ycoord = 100
bot_v = 1
count = 0

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 450)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")


rows = 50
arr = [None for j in range(rows)]  

  

for row in range(rows):  
     arr[row] = bot(xcoord,ycoord,3,5)
     xcoord = xcoord + 15
     if xcoord > 600:
        xcoord = 0
        ycoord = ycoord + 10
     
#next row       
print(arr)  

def drawalien(xcoord,ycoord):
    




done = False


clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    

    
    screen.fill(BLACK)
    
    for i in range(len(arr)):
            arr[i].x += bot_v
    count  = count + 1

    if count > 100:
        count = 0
        bot_v *= -1
        for i in range(len(arr)):
            arr[i].y += 20
            
    for i in range(len(arr)):
        pygame.draw.rect(screen, WHITE, (arr[i].x,arr[i].y,arr[i].size,arr[i].size)) 


    
    pygame.display.flip()

    
    clock.tick(60)


pygame.quit()