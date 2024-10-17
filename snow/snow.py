import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF



pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")
snow = 0
snowy = 0
snow2 = 50
snowy2 = 100
snow3 = 500
snowy3 = 300



done = False
def falling(y):
    y = y-5
    return y


def outofbounds(y,x):
    if y >= 500:
        y = 0
        x = random.randint(0,690)
        return y,x


clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True






    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [snow, snowy, 10, 10], 0)
    snowy = snowy +5
    if snowy >=500:
        snowy = 0
        snow = random.randint(0,690)
    

    pygame.draw.rect(screen, WHITE, [snow2, snowy2, 10, 10], 0)
    snowy2 = snowy2 +5
    if snowy2 >=500:
        snowy2 = 0
        snow2 = random.randint(0,690)
    
    pygame.draw.rect(screen, WHITE, [snow3, snowy3, 10, 10], 0)
    snowy3 = snowy3 +5
    if snowy3 >=500:
        snowy3 = 0
        snow3 = random.randint(0,690)
    
    pygame.display.flip()

    clock.tick(60)

# Close the window and quit.
pygame.quit()