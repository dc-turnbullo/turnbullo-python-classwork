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
pi = 3.141592658772397170284017237109779827308099865209818986239560981203791639817291838918747298374271798237091734798120779326918273012798366409124017598661030830912097598237981740973209175208168926387091259816629836981279010984091298446932650917092381569816239871092570162396129871092830912896561298709185798236951907928380165981263097109871962498173095701973216487638974091203971057983261912739817240971072309850723094810928857098218307185371098238128985781927093838582734712893801
pygame.display.set_caption("Is he short or is he not short")
circx = 700
circy = 200
momenty = -1
momentx = -1.75
grav = 0.1
yvelo = -1
up = True
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
    circx += momentx
    circy += momenty
    
    if circy < 20:
        diry = diry * -1
    
    if circx < 0:
        circx = 700
        diry = diry * -1
    

    
    pygame.display.flip()