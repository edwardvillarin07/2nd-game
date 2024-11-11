import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aircraft Bullet Dodge")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game settings
PLAYER_SIZE = 50
BULLET_SIZE = 10
BULLET_SPEED = 7
PLAYER_SPEED = 5

# Player setup
player = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_SIZE * 2, PLAYER_SIZE, PLAYER_SIZE)

# Bullet setup
bullets = []

# Timer
clock = pygame.time.Clock()
score = 0

# Font
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-PLAYER_SPEED, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(PLAYER_SPEED, 0)
    if keys[pygame.K_UP] and player.top > 0:
        player.move_ip(0, -PLAYER_SPEED)
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.move_ip(0, PLAYER_SPEED)

    # Bullet generation
    if random.randint(1, 30) == 1:
        bullet_x = random.randint(0, WIDTH - BULLET_SIZE)
        bullets.append(pygame.Rect(bullet_x, 0, BULLET_SIZE, BULLET_SIZE))

    # Move bullets
    for bullet in bullets[:]:
        bullet.move_ip(0, BULLET_SPEED)
        if bullet.colliderect(player):
            # End the game if hit
            running = False
        if bullet.top > HEIGHT:
            bullets.remove(bullet)
            score += 1

    # Draw player and bullets
    pygame.draw.rect(screen, BLUE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Game over message
screen.fill(BLACK)
game_over_text = font.render("Game Over", True, WHITE)
final_score_text = font.render(f"Your Score: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
screen.blit(final_score_text, (WIDTH // 2 - 80, HEIGHT // 2 + 20))
pygame.display.flip()

pygame.time.wait(2000)
pygame.quit()
