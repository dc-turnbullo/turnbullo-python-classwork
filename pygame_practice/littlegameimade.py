"""
Pygame Bullet Hell (Expanded Play Area & Random Mixed Attacks)
-------------------------------------------------------------
Features:
- Smaller player radius (6px)
- Expanded play area larger than the visible screen; player can move offscreen
- All three attack types occur randomly and continuously, overlapping and cycling
- Dash (LShift) and slow time (Space) retained

Run: python pygame_bullet_hell.py
"""

import math
import random
import pygame
from pygame.math import Vector2

# -------- CONFIG --------
SCREEN_W, SCREEN_H = 900, 700
FPS = 60
PLAYER_SPEED = 320
PLAYER_RADIUS = 6
PLAYER_COLOR = (50, 200, 255)
BULLET_COLOR = (255, 90, 90)
BULLET_RADIUS = 5
BULLET_DAMAGE = 1

# Attack timings
INCOMING_SPAWN_INTERVAL = 0.08
EXPLOSION_INTERVAL = 2.0
SPIRAL_SPAWN_INTERVAL = 0.04

# Expanded play area
PLAY_AREA_MARGIN = 400  # player can move beyond screen in this radius

# Slow time
SLOW_FACTOR = 0.28
SLOW_MAX = 4.0
SLOW_DRAIN_RATE = 1.0
SLOW_RECOVER_RATE = 0.6

# Dash
DASH_SPEED_MULT = 3.0
DASH_TIME = 0.18
DASH_COOLDOWN = 1.2

PLAYER_MAX_HEALTH = 10

BG = (18, 18, 20)
HUD_BG = (28, 28, 32)
WHITE = (230, 230, 230)

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Bullet Hell - Random Mixed Attacks | Dash: LSHIFT | Slow: SPACE")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)
big_font = pygame.font.SysFont(None, 36)

def clamp(x, a, b):
    return max(a, min(b, x))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, radius=BULLET_RADIUS, color=BULLET_COLOR, damage=BULLET_DAMAGE):
        super().__init__()
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.radius = radius
        self.color = color
        self.damage = damage
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, dt, time_scale=1.0):
        self.pos += self.vel * dt * time_scale
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        margin = 2000
        if (
            self.pos.x < -margin
            or self.pos.x > SCREEN_W + margin
            or self.pos.y < -margin
            or self.pos.y > SCREEN_H + margin
        ):
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = Vector2(SCREEN_W // 2, SCREEN_H - 120)
        self.radius = PLAYER_RADIUS
        self.color = PLAYER_COLOR
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=self.pos)
        self.vel = Vector2(0, 0)
        self.health = PLAYER_MAX_HEALTH
        self.dash_timer = 0.0
        self.dash_cooldown = 0.0
        self.invuln_timer = 0.0

    def update(self, dt, keys, time_scale=1.0):
        move = Vector2(0, 0)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x = 1
        if move.length_squared() > 0:
            move = move.normalize()

        speed = PLAYER_SPEED
        if self.dash_timer > 0:
            speed *= DASH_SPEED_MULT

        self.vel = move * speed
        self.pos += self.vel * dt * time_scale
        self.pos.x = clamp(self.pos.x, -PLAY_AREA_MARGIN, SCREEN_W + PLAY_AREA_MARGIN)
        self.pos.y = clamp(self.pos.y, -PLAY_AREA_MARGIN, SCREEN_H + PLAY_AREA_MARGIN)
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        if self.dash_timer > 0:
            self.dash_timer -= dt
            if self.dash_timer <= 0:
                self.invuln_timer = 0.0
        if self.dash_cooldown > 0:
            self.dash_cooldown -= dt
        if self.invuln_timer > 0:
            self.invuln_timer -= dt

    def dash(self):
        if self.dash_cooldown <= 0 and self.dash_timer <= 0:
            self.dash_timer = DASH_TIME
            self.dash_cooldown = DASH_COOLDOWN
            self.invuln_timer = DASH_TIME

    def hit(self, dmg):
        if self.invuln_timer > 0:
            return False
        self.health -= dmg
        return True


# Groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Timers and state
incoming_timer = 0.0
explosion_timer = 0.0
spiral_timer = 0.0
spiral_angle = 0.0

slow_energy = SLOW_MAX
slow_active = False


def spawn_incoming(player_pos):
    edge = random.choice(['top', 'bottom', 'left', 'right'])
    if edge == 'top':
        x = random.uniform(-100, SCREEN_W + 100)
        y = -120
    elif edge == 'bottom':
        x = random.uniform(-100, SCREEN_W + 100)
        y = SCREEN_H + 120
    elif edge == 'left':
        x = -120
        y = random.uniform(-100, SCREEN_H + 100)
    else:
        x = SCREEN_W + 120
        y = random.uniform(-100, SCREEN_H + 100)

    pos = Vector2(x, y)
    dir = (player_pos - pos).normalize()
    speed = random.uniform(140, 240)
    vel = dir * speed
    b = Bullet(pos, vel)
    bullets.add(b)
    all_sprites.add(b)


def spawn_explosion(point, count=36, speed=180):
    for i in range(count):
        ang = (i / count) * 2 * math.pi
        vel = Vector2(math.cos(ang), math.sin(ang)) * random.uniform(speed * 0.85, speed * 1.15)
        b = Bullet(point, vel)
        bullets.add(b)
        all_sprites.add(b)


def spawn_spiral(center, base_angle, count=1, speed=180, spread=0.12):
    for i in range(count):
        ang = base_angle + i * spread
        vel = Vector2(math.cos(ang), math.sin(ang)) * speed
        b = Bullet(center, vel)
        bullets.add(b)
        all_sprites.add(b)


def check_collisions():
    for b in bullets.sprites():
        if (b.pos - player.pos).length_squared() <= (b.radius + player.radius) ** 2:
            if player.hit(b.damage):
                b.kill()


def draw_hud(surf):
    pad = 8
    h = 68
    rect = pygame.Rect(0, SCREEN_H - h, SCREEN_W, h)
    pygame.draw.rect(surf, HUD_BG, rect)

    health_text = font.render(f"Health: {player.health}/{PLAYER_MAX_HEALTH}", True, WHITE)
    surf.blit(health_text, (pad, SCREEN_H - h + pad))

    bar_w = 240
    bar_h = 12
    x = pad
    y = SCREEN_H - h + pad + 26
    pygame.draw.rect(surf, (60, 60, 60), (x, y, bar_w, bar_h))
    filled = int((slow_energy / SLOW_MAX) * bar_w)
    pygame.draw.rect(surf, (100, 200, 100), (x, y, filled, bar_h))

    cd = max(0.0, player.dash_cooldown)
    cd_text = font.render(f"Dash CD: {cd:.1f}s", True, WHITE)
    surf.blit(cd_text, (x + 300, SCREEN_H - h + pad))

    if player.health <= 0:
        go = big_font.render("YOU DIED - R to Restart", True, (220, 50, 50))
        surf.blit(go, (SCREEN_W // 2 - go.get_width() // 2, SCREEN_H // 2 - go.get_height() // 2))


def reset_game():
    global bullets, all_sprites, player, incoming_timer, explosion_timer, spiral_timer, spiral_angle, slow_energy
    bullets.empty()
    all_sprites.empty()
    player = Player()
    all_sprites.add(player)
    incoming_timer = explosion_timer = spiral_timer = 0.0
    spiral_angle = 0.0
    slow_energy = SLOW_MAX


# Main loop
running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for e in events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
            if e.key == pygame.K_r and player.health <= 0:
                reset_game()
            if e.key == pygame.K_LSHIFT:
                player.dash()

    # Slow time
    if keys[pygame.K_SPACE] and slow_energy > 0 and player.health > 0:
        slow_active = True
        slow_energy = max(0, slow_energy - SLOW_DRAIN_RATE * dt)
    else:
        slow_active = False
        slow_energy = min(SLOW_MAX, slow_energy + SLOW_RECOVER_RATE * dt)

    time_scale = SLOW_FACTOR if slow_active else 1.0

    # Player update
    if player.health > 0:
        player.update(dt, keys, time_scale)

    # Random mixed attack patterns
    if player.health > 0:
        incoming_timer -= dt * (1.0 / time_scale)
        explosion_timer -= dt * (1.0 / time_scale)
        spiral_timer -= dt * (1.0 / time_scale)

        if incoming_timer <= 0:
            for _ in range(random.randint(1, 3)):
                spawn_incoming(player.pos)
            incoming_timer += random.uniform(0.05, 0.15)

        if explosion_timer <= 0:
            for _ in range(random.randint(1, 2)):
                point = Vector2(random.randint(0, SCREEN_W), random.randint(0, SCREEN_H))
                spawn_explosion(point, count=random.randint(20, 48), speed=random.randint(150, 230))
            explosion_timer += random.uniform(1.2, 2.5)

        if spiral_timer <= 0:
            for _ in range(random.randint(1, 2)):
                spawn_spiral(Vector2(random.randint(0, SCREEN_W), random.randint(0, SCREEN_H//2)), spiral_angle, count=2, speed=180)
                spiral_angle += 0.3
            spiral_timer += random.uniform(0.02, 0.05)

    # Update bullets
    for b in bullets.sprites():
        b.update(dt, time_scale)

    # Collisions
    if player.health > 0:
        check_collisions()

    # Drawing
    screen.fill(BG)

    # camera offset (center view on player)
    cam_x = clamp(player.pos.x - SCREEN_W / 2, -PLAY_AREA_MARGIN, PLAY_AREA_MARGIN)
    cam_y = clamp(player.pos.y - SCREEN_H / 2, -PLAY_AREA_MARGIN, PLAY_AREA_MARGIN)

    for b in bullets:
        pos = (b.rect.x - cam_x, b.rect.y - cam_y)
        screen.blit(b.image, pos)

    if not (player.invuln_timer > 0 and (pygame.time.get_ticks() // 80) % 2 == 0):
        screen.blit(player.image, (player.rect.x - cam_x, player.rect.y - cam_y))

    draw_hud(screen)

    pygame.display.flip()

pygame.quit()
