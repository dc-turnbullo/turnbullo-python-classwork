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

class projectile:
    def __init__(self,x_pos,y_pos,on,size) -> None:
        self.x = x_pos
        self.y = y_pos
        self.on = on
        self.size = size


counter = 0
xcoord = 0
ycoord = 100
bot_v = 1
count = 0
playerx = 330
playery = 430

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 450)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")


rows = 50
arr = [None for j in range(rows)]  
project = [None for j in range(rows)]


for row in range(rows):  
     project[row] = projectile(-100,900,0,5)
     

for row in range(rows):  
     arr[row] = bot(xcoord,ycoord,3,5)
     xcoord = xcoord + 15
     if xcoord > 600:
        xcoord = 0
        ycoord = ycoord + 10
     
#next row       
print(arr)  


def spawnprojectile(project,counter):
    project[counter].y = playery - 8
    project[counter].x = playerx + 18
    counter +=1
    counter = counter % 50
    return counter



done = False


clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            playerx +=1
        elif event.key == pygame.K_LEFT:
            playerx -=1
        elif event.key == pygame.K_SPACE:
           counter = spawnprojectile(project,counter)
           print("true")

    for i in range(rows):
        project[i].y -=1
        

    
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

    pygame.draw.rect(screen, WHITE, (playerx,playery,40,10))
    pygame.draw.rect(screen, WHITE, (playerx + 18,playery - 8, 4,8))
    pygame.display.flip()
    
    
    for i in range(len(project)):
        pygame.draw.rect(screen, WHITE, (project[i].x,project[i].y,project[i].size,project[i].size)) 
    clock.tick(60)


pygame.quit() 