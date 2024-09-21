import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width = 600
height = 400

# Create game window
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set clock and snake speed
clock = pygame.time.Clock()
snake_block = 10

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color, location):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, location)

def pause_game():
    pause = True 
    while pause :
        dis.fill(black)
        message("Game paused. Press 'p' to continue again", white, [width / 6, height / 3])
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

#
def game_manual():
    manual= True
    while manual:
        dis.fill(black) 
        message("Welcome to Snake Game!", white, [200, 100])
        message("Use arrow keys to move.", white, [207, 125])
        message("Eat one white food will earn you one point.", white, [130, 150])
        message("EATING RED FOOD WILL KILL YOUR SNAKE.", red, [120, 175])
        message("Type 's' to start, 'p' to pause and 'q' to quit", white, [130, 225])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    manual = False


# Game loop
def game_loop():

    snake_speed = 15

    game_over = False
    game_close = False

    # Initial position of snake
    x1 = width / 2
    y1 = height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body and initial length
    snake_list = []
    length_of_snake = 1

    # Initial position of food
    food1_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food1_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    food2_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food2_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red,[width / 6, height / 3])   
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    pause_game()

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, white, [food1_x, food1_y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [food2_x, food2_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food1_x and y1 == food1_y:
            food1_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food1_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            food2_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food2_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

            if (length_of_snake-1) % 10 == 0 and length_of_snake!= 1:
                snake_speed += 5

        if x1 == food2_x and y1 == food2_y:
            game_close= True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_manual()

# Run the game
game_loop()
