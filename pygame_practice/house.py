import pygame
import math
pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
fps = 60
white = (0xff, 0xff, 0xff)
red = (0xff, 0, 0)
green = (0x00,0xff,0x00)
brown = (0x96,0x4b,0x00)
yellow = (0xff,0xff,0x00)
pygame.display.set_caption("Is he short or is he not short")
Pi = 3.14120973109278509710293840917235091789287907153908910829371735290
circx = 700
circy = 200
momenty = ((1/100000) * (circx**2) +1) 
momentx = -1.75
yvelo = -1
up = True
dirx = 1
diry = -1
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    clock.tick(fps)
    screen.fill(white)
    pygame.draw.rect(screen, red, [280, 300, 100, 140], 0)
    pygame.draw.polygon(screen, green, ([280,300],[330,280] ,[380,300]))
    pygame.draw.rect(screen, brown, [325, 350, 30, 50], 0)
    pygame.draw.circle(screen, yellow, (circx, circy), 20, 0) 
    #x default value  == 700
    #y default value == 200
    #x goes 1.75 more than y 
    circx += momentx * dirx
    circy += momenty * diry
    momenty = ((1/100000) * (circx**2) +20) 
    pygame.draw.arc(screen, (255,255,255), [50,50,50,50], Pi/2, Pi, 2)
    if circy < 20:
        diry = diry * -1
    
    if circx < 0:
        circx = 700
        dirx = dirx * -1
        diry = diry * -1
    

    
    pygame.display.flip()