import pygame
import random
pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
fps = 120
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
yballspeed = 2
#p1 = paddel 1  tl top left x or y refer to axis
font = pygame.font.SysFont('Calibri', 25, True, False)

p1score = 0
p2score = 0
p1tlx = 10
p1tly = 150
p1xlen = 20
p1ylen = 70
Bounced = False
p2tlx = 670
p2tly = 150
p2xlen = 20
p2ylen = 70
def resetball(ballspeed,ballx,bally):
    ballspeed = 2
    ballx = 350
    bally = 200
    return ballspeed,ballx,bally


def resetbounce(ballx,Bounced):
    if ballx > 200 and ballx < 500:
        Bounced = False
    return Bounced

def randballspeed(xballspeed,yballspeed):
    xballspeed = random.randint(5,10)
    yballspeed = random.randint(5,10)
    return xballspeed,yballspeed

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
    bally = bally + (yballspeed * balldiry)
    p1tly = p1tly + (yballspeed * balldiry)
    
    if Bounced ==False:
        if ((ballx+20) >= p2tlx and (ballx+20)<= p2tlx + p2xlen) and (bally >= p2tly and bally <= p2tly + p2ylen):
            balldirx = balldirx * -1
            ballspeed = ballspeed + 0.5
            print("ball touched paddel")
            Bounced = True
        if ((ballx-20) >= p1tlx and (ballx-20)<= p1tlx + p1xlen) and (bally >= p1tly and bally <= p1tly + p1ylen):
            balldirx = balldirx * -1
            ballspeed = ballspeed + 0.5
            print("ball touched paddel")
            Bounced = True

    Bounced = resetbounce(ballx,Bounced)
    
    
    if bally <=0 or bally >= 400:
        balldiry *= -1
        ballspeed,yballspeed = randballspeed(ballspeed,yballspeed)
    
    text = font.render("Player 1 score: "+ str(p1score), p1score, True, red)
    text2 = font.render("Player 2 score: " + str(p2score), p2score, True, blue)

    screen.blit(text2, [500, 30])
    screen.blit(text, [30, 30])

    if ballx > 700:
        p1score +=1
        ballspeed,ballx,bally = resetball(ballspeed,ballx,bally)
        p1tlx = 10
        p1tly = 150
        

    
    if ballx<0:
        p2score +=1
        ballspeed,ballx,bally = resetball(ballspeed,ballx,bally)
        p1tlx = 10
        p1tly = 150
    
    pygame.display.flip()

