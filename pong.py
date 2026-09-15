import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

player = pygame.Rect(50, SCREEN_HEIGHT/2 - 45, 15, 90) # x, y, width, height
opponent = pygame.Rect(SCREEN_WIDTH - 65, SCREEN_HEIGHT/2 - 45, 15, 90) # x, y, width, height
ball = pygame.Rect(SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 -10, 20, 20)
ball_speed_x = 5
ball_speed_y = 5

player_score, opponent_score = 0, 0
game_font = pygame.font.Font(None, 74)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if ball.left < 0:
        opponent_score += 1
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_speed_x *= -1

    if ball.right > SCREEN_WIDTH:
        player_score += 1
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_speed_x *= -1


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.top > 0:
        player.y -= 6

    if keys[pygame.K_s] and player.bottom < SCREEN_HEIGHT:  
        player.y += 6

    if opponent.centery < ball.centery and opponent.bottom < SCREEN_HEIGHT:
        opponent.y += 5

    if opponent.centery > ball.centery and opponent.top > 0:
            opponent.y -= 5

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.rect(screen, RED, ball)
    score_text = game_font.render(f"{player_score} - {opponent_score}", True, WHITE)
    screen.blit(score_text, score_text.get_rect(center=((SCREEN_WIDTH / 2, 40))))
    pygame.display.flip()
    clock.tick(60)
    