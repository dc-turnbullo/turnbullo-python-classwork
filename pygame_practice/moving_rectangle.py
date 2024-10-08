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
movement= 5
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
        rtx +=movement
    if rtx >= 680:
        rtx = 0

    rtx += movement
    if rtx>= 680:
        rtx = 0
    pygame.display.flip()

    