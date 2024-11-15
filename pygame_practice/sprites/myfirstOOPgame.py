import pygame
import random
#rom pygame.sprite import _Group

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

class Block(pygame.sprite.Sprite):
    def __init__(self,colour,height,width) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

    def moveright(self):
        self.rect.x +=5
    
    def moveleft(self):
        self.rect.x -= 5
    
    def moveup(self):
        self.rect.y -= 5
    
    def movedown(self):
        self.rect.y += 5
    
    def reset_pos(self):
       
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, size[0])
    
    def update(self):
      
        self.rect.y += 5
        
        if self.rect.y > 410:
            self.reset_pos()
#endofclassblock


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK,20,15)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])

    block_list.add(block)
    all_sprites_list.add(block)


score = 0
player = Block(RED,20,15)
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player.moveright()
        elif event.key == pygame.K_LEFT:
            player.moveleft()
        elif event.key == pygame.K_UP:
            player.moveup()
        elif event.key == pygame.K_DOWN:
            player.movedown()
    screen.fill(WHITE)
   
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
    
        # Reset block to the top of the screen to fall again.
        block.reset_pos()
   
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()