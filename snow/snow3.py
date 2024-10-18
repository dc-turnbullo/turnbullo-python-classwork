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
    #endrecord





flake_v = 1

pygame.init()

# Set the width and height of the screen [width, height]
size = (1400, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


rows = 250
arr = [None for j in range(rows)]  

  

for row in range(rows):  
     arr[row] = Flake(random.randint(0,size[0]-1),random.randint(0,size[1]-1), random.randint(1,3),random.randint(0,10),random.randint(1,2))
#next row       
print(arr)  


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for i in range(len(arr)):
        if arr[i].y > size[1]:
            arr[i].y = 0
            arr[i].x = random.randint(0,size[0]-1)
        else:
            arr[i].y = arr[i].y + arr[i].vel
    #next i


    
    screen.fill(BLACK)
    
    for i in range(len(arr)):
        rand = random.randint(1,2)
        if arr[i].move & 2 == 0:
            arr[i].x = arr[i].x +1
            pygame.draw.rect(screen, WHITE, (arr[i].x,arr[i].y,arr[i].size,arr[i].size))  
        else:
            pygame.draw.rect(screen, WHITE, (arr[i].x,arr[i].y,arr[i].size,arr[i].size))
            arr[i].x = arr[i].x -1

    
    pygame.display.flip()

    
    clock.tick(60)


pygame.quit()