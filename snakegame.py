import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")


cell_size = 10

#create snake
snake_pos = [[int(SCREEN_WIDTH / 2 ),int(SCREEN_HEIGHT / 2)]]
snake_pos.append([int(SCREEN_WIDTH / 2 ),int(SCREEN_HEIGHT / 2) + cell_size ])
snake_pos.append([int(SCREEN_WIDTH / 2 ),int(SCREEN_HEIGHT / 2) + cell_size * 2 ])
snake_pos.append([int(SCREEN_WIDTH / 2 ),int(SCREEN_HEIGHT / 2) + cell_size  * 3])



def drawScreen():
    SCREEN.fill(bg_color)

snake_color = (3, 240, 252)
bg_color = (54, 2, 82)
direction = 1
update_snake = 0
food = [0,0]
food_color = ('red')
new_food = True
new_piece = [0,0]



run = True

while run:

    drawScreen()
    #movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction !=3:
                direction =  1
            if event.key == pygame.K_RIGHT and direction !=4:
                direction =  2
            if event.key == pygame.K_DOWN and direction !=1:
                direction =  3
            if event.key == pygame.K_LEFT and direction !=2:
                direction =  4
    
    #create food
    if new_food == True:
        new_food = False
        food[0] = cell_size * random.randint(0, (SCREEN_WIDTH / cell_size) -1)
        food[1] = cell_size * random.randint(0, (SCREEN_HEIGHT / cell_size) -1)


    #draw the food
    pygame.draw.rect(SCREEN, food_color, (food[0], food[1], cell_size,cell_size))

    #food eating:
    if snake_pos[0] == food:
        new_food = True
        new_piece = list(snake_pos[-1])
        if direction == 1:
            new_piece[1] += cell_size
        if direction == 3:
            new_piece[1] -= cell_size
        if direction == 2:
            new_piece[0] -= cell_size
        if direction == 4:
            new_piece[0] += cell_size

        snake_pos.append(new_piece)



    if update_snake > 99:
        update_snake =0
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        #headingup
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size
        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size
        

    #drawsnake
    head = 1
    for x in snake_pos:
        if head == 0 :
            pygame.draw.rect(SCREEN , snake_color, (x[0], x[1 ], cell_size , cell_size))
            pygame.draw.rect(SCREEN , snake_color, (x[0] + 1,x[1 ] + 1, cell_size - 2  , cell_size - 2))
        if head == 1:
            pygame.draw.rect(SCREEN , snake_color, (x[0], x[1 ], cell_size , cell_size))
            pygame.draw.rect(SCREEN , snake_color, (x[0] + 1,x[1 ] + 1, cell_size - 2  , cell_size - 2))
            head = 0



    pygame.display.update()
    update_snake += 1

pygame.quit()
