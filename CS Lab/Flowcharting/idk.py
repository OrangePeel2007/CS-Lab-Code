import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)

# Bird
bird_x, bird_y = 50, HEIGHT // 2
bird_radius = 15 
bird_velocity = 0
gravity = 0.5
jump = -8

# Pipes
pipe_width = 50
pipe_gap = 150
pipe_velocity = 3
pipes = []

score = 0
font = pygame.font.SysFont(None, 36)

def create_pipe():
    height = random.randint(100, 400)
    pipes.append([WIDTH, height])

def draw_pipes():
    for x, h in pipes:
        pygame.draw.rect(screen, GREEN, (x, 0, pipe_width, h))
        pygame.draw.rect(screen, GREEN, (x, h + pipe_gap, pipe_width, HEIGHT))

def move_pipes():
    global score
    for pipe in pipes:
        pipe[0] -= pipe_velocity
    if pipes and pipes[0][0] < -pipe_width:
        pipes.pop(0)
        score += 1

def check_collision():
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        return True
    for x, h in pipes:
        if (bird_x + bird_radius > x and bird_x - bird_radius < x + pipe_width and
           (bird_y - bird_radius < h or bird_y + bird_radius > h + pipe_gap)):
            return True
    return False

running = True
frame_count = 0
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = jump

    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity

    # Pipe logic
    frame_count += 1
    if frame_count % 90 == 0:
        create_pipe()
    move_pipes()

    # Draw
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)
    draw_pipes()
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Check collision
    if check_collision():
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
