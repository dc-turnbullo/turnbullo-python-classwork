### SRC - Good work, but read my comments?
import pygame
import math ### SRC - Did you use this for a previous version? OT - it is
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
### SRC - you can use math.pi instead.
Pi = 3.14120973109278509710293840917235091789287907153908910829371735290
circx = 700
circy = 200
momenty = -70
momentx = -110
yvelo = -1
up = True
dirx = 1
diry = 1
grav = 1
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    ''' SRC - This code works, but typically you would put in a 
        different order:
        (1) Update variable values
        (2) Black screen
        (3) Draw shapes
        (4) Clock.tick
        OT - it is just the order that i coppied the original starting code from that arcade games website with, i think i do it differently in the other projects
    '''
    clock.tick(fps)
    screen.fill(white)
    pygame.draw.rect(screen, red, [280, 300, 100, 140], 0)
    pygame.draw.polygon(screen, green, ([280,300],[330,280] ,[380,300]))
    pygame.draw.rect(screen, brown, [325, 350, 30, 50], 0)
    pygame.draw.circle(screen, yellow, (circx, circy), 20, 0) 
    #x default value  == 700
    #y default value == 200
    #x goes 1.75 more than y 
    circx += (momentx * dirx)//32
    circy += (momenty * diry)//32
    
    if circy < 20:
        diry = diry * -1
    
    momenty = momenty + grav
    
    if circx < 0:
        circx = 700
        momenty = -70
    

    
    pygame.display.flip()