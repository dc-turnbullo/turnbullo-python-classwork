import pygame
import random

BLACK = 0x000000
WHITE = 0xFFFFFF

class Bot:
    def __init__(self, x_pos, y_pos, velocity, size, on):
        self.x = x_pos
        self.y = y_pos
        self.vel = velocity
        self.size = size
        self.on = on

class Projectile:
    def __init__(self, x_pos, y_pos, on, size):
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

size = (700, 450)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")

rows = 50
arr = [None for j in range(rows)]
project = [Projectile(-100, 900, False, 5) for i in range(rows)]

for row in range(rows):
    arr[row] = Bot(xcoord, ycoord, 3, 5, True)
    xcoord += 15
    if xcoord > 600:
        xcoord = 0
        ycoord += 10

def spawn_projectile(project, counter):
    if not project[counter].on:
        project[counter].y = playery - 8
        project[counter].x = playerx + 18
        project[counter].on = True
        counter = (counter + 1) % rows
    return counter

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                counter = spawn_projectile(project, counter)
    
    
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerx += 5
        elif event.key == pygame.K_LEFT:
            playerx -= 5




    for i in range(rows):
        if project[i].on:
            project[i].y -= 5
            if project[i].y < 0:
                project[i].on = False

    for i in range(len(arr)):
        arr[i].x += bot_v
    count += 1

    if count > 100:
        count = 0
        bot_v *= -1
        for i in range(len(arr)):
            arr[i].y += 20

    screen.fill(BLACK)
    
    for bot in arr:
        if bot.on:
            pygame.draw.rect(screen, WHITE, (bot.x, bot.y, bot.size, bot.size))
    
    pygame.draw.rect(screen, WHITE, (playerx, playery, 40, 10))

    for proj in project:
        if proj.on:
            pygame.draw.rect(screen, WHITE, (proj.x, proj.y, proj.size, proj.size))

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
