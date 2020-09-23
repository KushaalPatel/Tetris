import pygame
import time
import random

####NOTES#####
# - add buttons - DID IT
# - make background a better shade of blue - DID IT
# - link to other screens


pygame.init()

display_width = 800
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (108, 214, 254)
block_color = (53, 115, 255)
ltgreen = (108, 208, 121)
drkgreen = (0, 185, 2)
medpink = (254, 134, 154)
drkpink = (253, 106, 158)

startFont = pygame.font.SysFont("bodoniblack", 72)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

tetImg = pygame.image.load('imgs/tetris99.png')

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
    else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def tet(x, y):
    gameDisplay.blit(tetImg, (x, y))

x = -240
y = (display_height*.1)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(blue)
        tet(x, y)

        button("Start!", 100, 450, 200, 100, ltgreen, drkgreen)
        button("Help", 500, 450, 200, 100, medpink, drkpink)

        pygame.display.update()
        clock.tick(15)

game_intro()