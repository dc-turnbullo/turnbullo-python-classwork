import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = 0x0000ff
pygame.init()
randcolour = False


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
        self.rect.x +=3
    
    def moveleft(self):
        self.rect.x -= 3
    
    def moveup(self):
        self.rect.y -= 3
    
    def movedown(self):
        self.rect.y += 3
    
    def movemouse(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos

    def reset_pos(self):
       
        self.rect.y = 0
    
    def rand_pos(self):
        self.rect.y = random.randrange(size[1])
        self.rect.x = random.randrange(size[0])    
    def update(self):
        
        self.rect.y += 1
        
        if self.rect.y >500:
            self.reset_pos()
    
    def changecolour(self,colour):
        self.image.fill(colour)

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def timeleftdpl(timeleft,font):
    tml = font.render(f"Time left: {timeleft//60}", True, GREEN, WHITE)
    textRect = tml.get_rect()
    textRect.center = ( 100, 40)
    screen.blit(tml, textRect)

def dopaminetime():
    for Blocks in block_list:
        colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        Block.changecolour(colour)


def endscreentext(score,font):
    endtext = font.render(f"Game Over your score = {score}", True, GREEN, BLUE)
    textRect = endtext.get_rect()
    textRect.center = ( 700// 2, 400 // 2)
    screen.fill(BLACK)
    screen.blit(endtext, textRect)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.display.flip()

 
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK,20,15)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])

    block_list.add(block)
    all_sprites_list.add(block)

dopamine = Block(BLUE,20,20)
dopamine.rect.x = random.randrange(size[0])
dopamine.rect.y = random.randrange(size[1])
block_list.add(dopamine)
all_sprites_list.add(dopamine)



player = Block(RED,20,15)
all_sprites_list.add(player)
timeleft = 36
done = False

clock = pygame.time.Clock()


def gameplay():
    screen.fill(WHITE)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
    
        # Reset block to the top of the screen to fall again.
        block.rand_pos()
    for block in block_list:
        block.update()
    all_sprites_list.draw(screen)
    player.movemouse()
    pygame.display.flip()

# -------- Main Program Loop --------------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    

    screen.fill(WHITE)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
        if block == dopamine:
            randcolour = True
            startscore = timeleft
        
        # if randcolour == True:
        #     dopaminetime()
        #     if startscore - score > 600:
        #         randcolour = False


        # Reset block to the top of the screen to fall again.
        block.rand_pos()
    for block in block_list:
        block.update()
   
   
    timeleftdpl(timeleft,font)
    all_sprites_list.draw(screen)
    player.movemouse()
    
    
    while timeleft <= 0:
        endscreentext(score,font)
        
    pygame.display.flip()
    

    clock.tick(60)
    timeleft -=1


pygame.quit()