import pygame
import sys
import random

# start thingy
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("2D Racing Game")

# Colours
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Car drawing
car_width = 50
car_height = 90
car = pygame.Rect(WIDTH // 2 - car_width // 2, HEIGHT - car_height - 10, car_width, car_height)
car_speed = 5

# Track drawing
road_width = 300
road_left = WIDTH // 2 - road_width // 2
road_right = WIDTH // 2 + road_width // 2
line_height = 40
line_gap = 20
lines = [pygame.Rect(WIDTH // 2 - 5, y, 10, line_height) for y in range(0, HEIGHT, line_height + line_gap)]

# distance
distance = 0
font = pygame.font.SysFont(None, 40)

def draw_road():
    screen.fill(GREEN)
    pygame.draw.rect(screen, GRAY, (road_left, 0, road_width, HEIGHT))

    for line in lines:
        pygame.draw.rect(screen, WHITE, line)

def draw_car():
    pygame.draw.rect(screen, RED, car)

def draw_score():
    score_text = font.render(f"Distance: {distance}", True, WHITE)
    screen.blit(score_text, (10, 10))

def move_lines():
    for line in lines:
        line.y += car_speed
        if line.y > HEIGHT:
            line.y = -line_height - line_gap

# Game 
running = True
while running:
    clock.tick(60)
    move_lines()
    distance += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # balls bro
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.left > road_left:
        car.x -= car_speed
    if keys[pygame.K_RIGHT] and car.right < road_right:
        car.x += car_speed

    draw_road()
    draw_car()
    draw_score()
    pygame.display.flip()

pygame.quit()
sys.exit()
