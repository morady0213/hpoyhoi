import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))
#icon
pygame.display.set_caption("Island escape")
icon = pygame.image.load('island.png')
pygame.display.set_icon(icon)
#arena
Grey=(128 , 128 ,128)
Green=(0,255,0)
Black=(0,0,0)
# player
player_img = pygame.image.load('rat.png')
playerX = 420
playerY = 200
playerX_change = 0
playerY_change = 0
step=0.1


def player(x,y):
    screen.blit(player_img, (x, y))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed chek if right or left
        if event.type == pygame.KEYDOWN:
            #print("Key stroke is preesed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # if keystroke is pressed chcek if up or down
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                playerY_change = -0.8
            if event.key == pygame.K_DOWN:
                playerY_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    # Checking the poundray of the space ship
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerY >= 736:
        playerY = 736
    playerY += playerY_change


    screen.fill((0,0,255))
    pygame.draw.rect(screen,Grey,[100,100,600,400])
    pygame.draw.rect(screen, Green, [700, 300, 100, 100])
    pygame.draw.line(screen, Black, (100, 100), (700, 100), 2)
    pygame.draw.line(screen, Black, (100, 200), (700, 200), 2)
    pygame.draw.line(screen, Black, (100, 300), (700, 300), 2)
    pygame.draw.line(screen, Black, (100, 400), (700, 400), 2)
    pygame.draw.line(screen, Black, (100, 500), (700, 500), 2)
    pygame.draw.line(screen, Black, (100, 200), (700, 200), 2)
    pygame.draw.line(screen, Black, (100, 100), (100, 500), 2)
    pygame.draw.line(screen, Black, (200, 100), (200, 500), 2)
    pygame.draw.line(screen, Black, (300, 100), (300, 500), 2)
    pygame.draw.line(screen, Black, (400, 100), (400, 500), 2)
    pygame.draw.line(screen, Black, (500, 100), (500, 500), 2)
    pygame.draw.line(screen, Black, (600, 100), (600, 500), 2)
    pygame.draw.line(screen, Black, (700, 100), (700, 500), 2)

    '''if (posX >= 700) and  (posY >= 300):
        print("you win")'''


    player(playerX,playerY)
    if posX >= playerX and posY>=playerY :
        print("You loss")
        screen.fill((0, 0, 0))
        pygame.quit()
    if  playerX<=100 or playerX>=740 or playerY<=100 or playerY>=450:
        print("you lose")
        screen.fill((0, 0,0))
        time.sleep(2)
        pygame.quit()
        #pygame.display.update()
    if (playerY>=300 and playerY<=400) and (playerX>=700): #and playerX<=800):
        print("win")
        screen.fill((255,255,255))
        time.sleep(2)
        pygame.quit()
        # pygame.display.update()

    pygame.display.update()