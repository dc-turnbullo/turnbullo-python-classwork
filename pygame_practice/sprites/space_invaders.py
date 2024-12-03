import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = 0x0000ff
pygame.init()
randcolour = False
rightvelo = 3
leftvelo = -3
defvelo = 0
gc = 0


size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

class Block(pygame.sprite.Sprite):
    def __init__(self,colour,height,width,velo) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velo = velo


    def move(self,velochange):
        self.velo = velochange


    

    def reset_pos(self):
       
        self.rect.y = 0
    
    def rand_pos(self):
        self.rect.y = random.randrange(size[1])
        self.rect.x = random.randrange(size[0])    
    def update(self):
        if self.rect.x >=0 and self.rect.x <= 700:
            self.rect.x += self.velo
        elif self.rect.x >=700:
            self.rect.x = 1
        else:
            self.rect.x = 699
        
        
    
    def changecolour(self,colour):
        self.image.fill(colour)


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        self.image = pygame.Surface([4,8])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.yvelo = 4
    
    def update(self):
        self.rect.y -= self.yvelo
        


score = 0
font = pygame.font.Font('freesansbold.ttf', 32)





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
bullet_list = pygame.sprite.Group()
xcoord = 0
ycoord = 20
for i in range(100):
    if xcoord >= 700:
        xcoord = 0
        ycoord += 35
    
    block = Block(BLACK,15,15,1)
    block.rect.x = xcoord
    block.rect.y = ycoord
    xcoord += 35

    block_list.add(block)
    all_sprites_list.add(block)




player = Block(RED,20,15,defvelo)
player.rect.x = 0
player.rect.y = 450
all_sprites_list.add(player)
timeleft = 0
done = False

clock = pygame.time.Clock()


def gameplay():
    screen.fill(WHITE)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    
    
    for block in blocks_hit_list:
        score += 1
        print(score)
    
        
    
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Projectile()
                bullet.rect.x = player.rect.x + 5
                bullet.rect.y = player.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            elif event.key == pygame.K_RIGHT: 
                player.move(rightvelo)
                print("moving right")
            elif event.key == pygame.K_LEFT:
                player.move(leftvelo)
                print("moving left")
        
    
    screen.fill(WHITE)


    for bullet in bullet_list:
        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
    
        for block in blocks_hit_list:
            score += 1
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            
            

        
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        
    
 
                


        


    all_sprites_list.draw(screen)
    
    
    # while timeleft < 0:
    #     endscreentext(score,font)
    block_list.update()
    bullet_list.update()
    all_sprites_list.update()
    pygame.display.flip()
    player.update()
    
    clock.tick(60)
    timeleft +=1
    
    if timeleft % 200 == 0:
        for block in block_list:
            block.velo *= -1
            block.rect.y += 10


pygame.quit()