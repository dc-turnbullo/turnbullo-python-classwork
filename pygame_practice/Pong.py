import pygame
pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
fps = 60
white = (0xff, 0xff, 0xff)
red = (0xff, 0, 0)
black = (0x00,0x00,0x00)
pygame.display.set_caption("Pong")
ballx = 350
bally = 200
balldirx = 1
balldiry = -1
ballspeed = 2
#p1 = paddel 1  tl top left x or y refer to axis
p1tlx = 0
p1tly = 150
p1blx = 0
p1bly = 250
p1brx = 30
p1bry = 250
p1trx = 30
p1try = 150

p2tlx = 670
p2tly = 150
p2blx = 670
p2bly = 250
p2brx = 700
p2bry = 250
p2trx = 700
p2try = 150
def p2movedown(p2bry,p2try,p2tly,p2bly):
    p2bry+=5
    p2try+=5
    p2tly+=5
    p2bly+=5
    return p2bry,p2try,p2tly,p2bly

def p2moveup(p2bry,p2try,p2tly,p2bly):
    p2bry-=5
    p2try-=5
    p2tly-=5
    p2bly-=5
    return p2bry,p2try,p2tly,p2bly

def p1movedown(p1bry,p1try,p1tly,p1bly):
    p1bry+=5
    p1try+=5
    p1tly+=5
    p1bly+=5
    return p1bry,p1try,p1tly,p1bly

def p1moveup(p1bry,p1try,p1tly,p1bly):
    p1bry-=5
    p1try-=5
    p1tly-=5
    p1bly-=5
    return p1bry,p1try,p1tly,p1bly

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True                
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            p2bry,p2try,p2tly,p2bly = p2movedown(p2bry,p2try,p2tly,p2bly)
        elif event.key == pygame.K_DOWN:
            p2bry,p2try,p2tly,p2bly = p2moveup(p2bry,p2try,p2tly,p2bly)
        
            #p1bry,p1try,p1tly,p1bly = p1movedown(p1bry,p1try,p1tly,p1bly)      
            #p1bry,p1try,p1tly,p1bly = p1moveup(p1bry,p1try,p1tly,p1bly)  
        
    
    clock.tick(fps)
    screen.fill(black)
    pygame.draw.circle(screen, white, (ballx, bally), 20, 0)
    pygame.draw.polygon(screen, white, ([p1tlx,p1tly],[p1blx,p1bly] ,[p1brx,p1bry],[p1trx,p1try]))
    pygame.draw.polygon(screen, white, ([p2tlx,p2tly],[p2blx,p2bly] ,[p2brx,p2bry],[p2trx,p2try]))
    ballx = ballx +(ballspeed * balldirx)
    bally = bally + (ballspeed * balldiry)

    #top one no work so i think we go witht the better solution
    if ballx in range(p2blx,p2trx) and bally in range(p2bly,p2try):
        balldirx *= -1
    
    if bally <=0 or bally >= 400:
        balldiry *= -1
    pygame.display.flip()

