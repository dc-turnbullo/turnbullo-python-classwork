import pygame
pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
fps = 60
white = (0xff, 0xff, 0xff)
red = (0xff, 0, 0)
pi = 3.14159265
pygame.display.set_caption("Ozin Is short!!")
rtx = 55
rty = 50
brx = 20
bry = 25
movement= 10
movementy = 10
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    clock.tick(fps)
    screen.fill(white)
    pygame.draw.rect(screen, red, [rtx, rty, brx, bry], 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        rtx +=movement
    if event.type == pygame.KEYDOWN:
        rty +=movementy
    if rtx >= 680 or rtx <= 0:
        movement = movement * -1
        brx += 5
        bry += 5
        if movement < 0:
            movement -=1
        else: 
            movement +=1
    if rty <=0 or rty >= 390:
        movementy *= -1
        bry += 5
        brx +=5
        if movementy < 0:
            movementy -=1
        else: 
            movementy +=1
    pygame.display.flip()

    