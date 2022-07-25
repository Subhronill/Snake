import pygame
import random
import os
pygame.mixer.init()
pygame.init()
#colors
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
white = (255, 255, 255)
#creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
#bg image
# bgimg = pygame.image.load('C:\\Users\\user\\Desktop\\Python\\MEGA\\FLAPPY BIRD\\images\\back.jpg')
# bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
pygame.display.set_caption("Snake")
pygame.display.update()
#game specific values
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def screen_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])
def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, red, [x, y, snake_size, snake_size])
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((5, 184, 229 ))
        screen_score("Welcome to Snakes by Sohom", black, 170,220)
        screen_score("Press ENTER to play", black, 250,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # pygame.mixer.music.load('music\\we_are.mp3')
                    # pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
#gameloop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    fps = 60
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 3
    snk_list = []
    # checking the file existence
    with open("highscore.txt", "r") as f:
        if (not os.path.exists("highscore.txt")):
            with open("highscore.txt", 'w') as f:
                f.write("0")
        with open("highscore.txt", 'r') as f:
            hi_score = f.read()
    snake_length = 1
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(hi_score))
            gameWindow.fill(white)
            screen_score("GAME OVER : Press enter to continue", red, screen_width/8, screen_height/2.5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x  = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x  = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 50
            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10    
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snake_length += 5
                if score > int(hi_score):
                    hi_score = score
            gameWindow.fill(black)
            # gameWindow.blit(bgimg, (0, 0))
            screen_score(f"Score : {score }  |  Highscore : {hi_score}", cyan, 5, 5)
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snake_length:
                del snk_list[0]           
            if head in snk_list[:-1]:
                game_over = True
                # pygame.mixer.music.load('music\\game_over.mp3')
                # pygame.mixer.music.play()
            if snake_x <0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                # pygame.mixer.music.load('music\\game_over.mp3`                                                                                                                                                                                                                                                                                        ')
                # pygame.mixer.music.play()
            # pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, red, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
# gameloop()