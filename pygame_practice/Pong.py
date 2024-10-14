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
blue = (0x00,0x00,0xff)
pygame.display.set_caption("Pong")
ballx = 350
bally = 200
balldirx = 1
balldiry = -1
ballspeed = 2
#p1 = paddel 1  tl top left x or y refer to axis
font = pygame.font.SysFont('Calibri', 25, True, False)

p1score = 0
p2score = 0
p1tlx = 10
p1tly = 150
p1xlen = 20
p1ylen = 70

p2tlx = 670
p2tly = 150
p2xlen = 20
p2ylen = 70

def p2movedown(p2tly):
    p2tly+=5
    return p2tly

def p2moveup(p2tly):
    p2tly-=5
    return p2tly

def p1movedown(p1tly):
    p1tly+=5
    
    return p1tly

def p1moveup(p1tly):
    p1tly-=5
    return p1tly
touched = False
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True                
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            p2tly = p2moveup(p2tly)
        elif event.key == pygame.K_DOWN:
            p2tly = p2movedown(p2tly)
        
            #p1bry,p1try,p1tly,p1bly = p1movedown(p1bry,p1try,p1tly,p1bly)      
            #p1bry,p1try,p1tly,p1bly = p1moveup(p1bry,p1try,p1tly,p1bly)  
        
    
    clock.tick(fps)
    screen.fill(black)
    pygame.draw.circle(screen, white, (ballx, bally), 20, 0)
    
    pygame.draw.rect(screen, red, [p1tlx, p1tly,p1xlen, p1ylen], 0)
    pygame.draw.rect(screen, blue, [p2tlx, p2tly, p2xlen, p2ylen], 0)
    
    ballx = ballx +(ballspeed * balldirx)
    bally = bally + (ballspeed * balldiry)
    p1tly = p1tly + (ballspeed * balldiry)
    
    if (ballx >= p2tlx and ballx<= p2tlx + p2xlen) and (bally >= p2tly and bally <= p2tly + p2ylen):
        balldirx = balldirx * -1
        ballspeed = ballspeed + 1
        print("ball touched paddel")
    
    if (ballx >= p1tlx and ballx<= p1tlx + p1xlen) and (bally >= p1tly and bally <= p1tly + p1ylen):
        balldirx = balldirx * -1
        ballspeed = ballspeed + 1
        print("ball touched paddel")
    
    
    if bally <=0 or bally >= 400:
        balldiry *= -1
        touched = False
    
    text = font.render("Player 1 score: ", p1score, True, red)
    text = font.render("Player 2 score: ", p2score, True, blue)


    pygame.display.flip()

