import  pygame

pygame.init()

Screen_width = 900
Screen_height = 600

screen = pygame.display.set_mode((Screen_width, Screen_height))

player = pygame.Rect((300, 300, 10, 70  ))
run = True

while run:

    screen.fill(("black"))

    pygame.draw.rect(screen, ("blue"), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quite()