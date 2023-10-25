import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Arkanoid")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
paddle = pygame.Rect(WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
BALL_RADIUS = 10
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_RADIUS, WINDOW_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 5
ball_speed_y = -5

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 5
    if keys[pygame.K_RIGHT] and paddle.right < WINDOW_WIDTH:
        paddle.right += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball off the walls
    if ball.left < 0 or ball.right > WINDOW_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top < 0:
        ball_speed_y = -ball_speed_y

    # Bounce the ball off the paddle
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # Game over if ball hits bottom of screen
    if ball.bottom > WINDOW_HEIGHT:
        pygame.quit()
        sys.exit()

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the paddle and ball
    pygame.draw.rect(window, (255, 255, 255), paddle)
    pygame.draw.circle(window, (255, 255, 255), (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)