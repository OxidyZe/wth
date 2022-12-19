import pygame
import sys
import clock
from button import Button

pygame.init()

img = pygame.image.load("pixelSpace.png")

screenWidth = 1280
screenHeight = 720
rowsBox = 9
rowsRec = 3
slots = 5
black = (0, 0, 0)
white = (255, 255, 255)
xCraft = 30
yCraft = 50

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Keppler Satellite Manager")
BG = pygame.image.load("assets/Background.png")

def getFont(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def mainMenu():
    while True:
        window.blit(BG, (0, 0))

        menuMousePos = pygame.mouse.get_pos()

        menuText = getFont(100).render("MAIN MENU", True, "#b68f40")
        menuRect = menuText.get_rect(center=(640, 100))

        playButton = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=getFont(75), base_color="#d7fcd4", hovering_color="White")
        optionsButton = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=getFont(75), base_color="#d7fcd4", hovering_color="White")
        quitButton = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=getFont(75), base_color="#d7fcd4", hovering_color="White")

        window.blit(menuText, menuRect)

        for button in [playButton, optionsButton, quitButton]:
            button.changeColor(menuMousePos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    play()
                if optionsButton.checkForInput(menuMousePos):
                    pass
                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play():
    def drawGrid(width, cellHeight, cellWidth, surface, rowsBox):
        x = 100
        y = 100


        for i in range(rowsBox):
            x += cellWidth
            y += cellHeight

            pygame.draw.line(surface, (255, 255, 255), (x, 120), (x, width))
            pygame.draw.line(surface, (255, 255, 255), (120, y), (width, y))

    xCraft = 30
    yCraft = 50
    rect = img.get_rect(center = (60, 80))
    moving = False

    while True:
        playPos = pygame.mouse.get_pos()

        window.fill(black)

        playBack = Button(image=None, pos=(1220, 700),text_input="BACK", font=getFont(30), base_color="White", hovering_color="Green")

        playBack.changeColor(playPos)
        playBack.update(window)

        window.blit(img, rect)
        drawGrid(280, 20, 20, window, rowsBox)
        length = 60
        for i in range (slots):
            pygame.draw.rect(window, white, (30, 50, 60, length), 1)
            length = length + 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playBack.checkForInput(playPos):
                    mainMenu()
            if event.type == pygame.MOUSEBUTTONUP:
                moving = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                rect.collidepoint(event.pos)
                moving = True
            elif event.type == pygame.MOUSEMOTION and moving:
                rect.move_ip(event.rel)
        pygame.display.update()

mainMenu()