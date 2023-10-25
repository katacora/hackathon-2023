import sys
import random
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake
SNAKE_SIZE = 20
snake = [pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, SNAKE_SIZE, SNAKE_SIZE)]
snake_direction = "right"

# Set up the food
FOOD_SIZE = 20
food = pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE), random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the snake
    if snake_direction == "right":
        new_head = pygame.Rect(snake[-1].x + SNAKE_SIZE, snake[-1].y, SNAKE_SIZE, SNAKE_SIZE)
    elif snake_direction == "left":
        new_head = pygame.Rect(snake[-1].x - SNAKE_SIZE, snake[-1].y, SNAKE_SIZE, SNAKE_SIZE)
    elif snake_direction == "up":
        new_head = pygame.Rect(snake[-1].x, snake[-1].y - SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
    elif snake_direction == "down":
        new_head = pygame.Rect(snake[-1].x, snake[-1].y + SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)

    # Check if the snake hit the wall
    if new_head.left < 0 or new_head.right > WINDOW_WIDTH or new_head.top < 0 or new_head.bottom > WINDOW_HEIGHT:
        pygame.quit()
        sys.exit()

    # Check if the snake hit itself
    if new_head in snake:
        pygame.quit()
        sys.exit()

    # Check if the snake ate the food
    if new_head.colliderect(food):
        food.x = random.randint(0, WINDOW_WIDTH - FOOD_SIZE)
        food.y = random.randint(0, WINDOW_HEIGHT - FOOD_SIZE)
    else:
        snake.pop(0)

    # Add the new head to the snake
    snake.append(new_head)

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and snake_direction != "left":
        snake_direction = "right"
    elif keys[pygame.K_LEFT] and snake_direction != "right":
        snake_direction = "left"
    elif keys[pygame.K_UP] and snake_direction != "down":
        snake_direction = "up"
    elif keys[pygame.K_DOWN] and snake_direction != "up":
        snake_direction = "down"

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the snake and food
    for segment in snake:
        pygame.draw.rect(window, (255, 255, 255), segment)
    pygame.draw.rect(window, (255, 0, 0), food)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(10)