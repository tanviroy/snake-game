# Author: Tanvi Roy
# Release Date: 31st March 2020
#====================================================================
import pygame, random, time, sys
from pygame.locals import *
pygame.mixer.pre_init(44100,-16,1,512)
pygame.mixer.init()
pygame.init()

Clock = pygame.time.Clock()
#====================================================================
# dimensions of the display screen
display_height = 600
display_width  = 800

snake_size  = 10 
snake_speed = 17

# colors 
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
white = (255,255,255)
black = (0,0,0)

font_style = pygame.font.SysFont("comicsans", 32)
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("It\'s Snakey Time")
#====================================================================

def message(msg, color):
    msg = font_style.render(msg, True, color)
    display.blit(msg, [display_width / 5.5, display_height / 2])

def snakey(snake_size, snake_count): 
    for x in snake_count:
        pygame.draw.rect(display, green, [x[0], x[1], snake_size, snake_size])

def main(): # game loop
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2
    x1_change = 0       
    y1_change = 0

    snake_count = []
    snake_length = 1
    score = 0
    
    sound_eat = pygame.mixer.Sound('yummy.wav')
    sound_die = pygame.mixer.Sound('end.wav')

    foodx = round(random.randrange(0, display_width - (snake_size * 3)) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - (snake_size * 3)) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            message("You Lost! Press C to Play Again or Q to Quit Game", white)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        game_over = True
                        print("Your final score is:", score)
                        pygame.quit()
                        sys.exit()
                    if event.key == K_c:
                        main()
                if event.type == QUIT:
                    game_over = True
                    print("Your final score is:", score)
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_LEFT and x1_change != snake_size:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == K_RIGHT and x1_change != -snake_size:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == K_DOWN and y1_change != -snake_size:
                    y1_change = snake_size
                    x1_change = 0
                elif event.key == K_UP and y1_change != snake_size:
                    y1_change = -snake_size
                    x1_change = 0

            if event.type == QUIT:
                game_over = True
                print("Your final score is:", score)
                pygame.quit()
                sys.exit()

        x1 += x1_change
        y1 += y1_change

        display.fill(black)
        pygame.draw.line(display, red, (0,0),(0,display_height),10)
        pygame.draw.line(display, red, (0,display_height),(display_width,display_height),10)
        pygame.draw.line(display, red, (display_width,display_height),(display_width,0),10)
        pygame.draw.line(display, red, (display_width,0),(0,0),10)
        pygame.draw.rect(display, green, [x1, y1, snake_size, snake_size])

        # snake movement 
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_count.append(snake_head) 
        if len(snake_count) > snake_length:
            del snake_count[0]

        snakey(snake_size, snake_count) # calls snake function 

        # eat randomly appearing food and grow
        pygame.draw.rect(display, red, [foodx, foody, snake_size, snake_size])
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - (snake_size * 3)) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - (snake_size * 3)) / 10.0) * 10.0
            sound_eat.play()
            snake_length += 1
            score += 1

        # boundaries 
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
            sound_die.play()
            
        pygame.display.update()

        Clock.tick(snake_speed)

    pygame.quit()
    quit()

#====================================================================

# _____   ____   __  __  _    _  ___
#   |    |____|  | \ |    \  /    |
#   |    |    |  |  \|     \/    _|_
#                                      

main()