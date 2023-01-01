import pygame
import random

from Tut8 import clock

pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Game Title
pygame.display.set_caption("SnakeGame!")
pygame.display.update()


font = pygame.font.SysFont(None, 60)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to Snake", black, 200, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

        pygame.display.update()
        clock.tick(30)

#Game Loop
def gameLoop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    snake_list = []
    snake_length = 1

    with open("HiScore.txt", "r") as f:
        HiScore = f.read()

    snake_size = 10

    food_x = random.randint(20, screen_width / 1.5)
    food_y = random.randint(20, screen_height / 1.5)
    score = 0
    init_velocity = 5

    clock = pygame.time.Clock()
    fps = 30

    while not exit_game:
        if game_over:
            with open("HiScore.txt", "w") as f:
                f.write(str(HiScore))

            gameWindow.fill(white)
            text_screen("Game over! Press to continue", red, screen_width/5, screen_height/5)

            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()

        else:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(20, screen_width / 1.5)
                food_y = random.randint(20, screen_height / 1.5)
                snake_length += 5

                if score > int(HiScore):
                    HiScore = score


            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "  Hiscore: " + str(HiScore), red, 5, 5)
            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del  snake_list[0]

            if head in snake_list[:-1]:
                game_over = True


            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                 game_over = True

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

#welcome()
gameLoop()