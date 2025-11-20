# Example file showing a basic pygame "game loop"
#import os
import pygame

# pygame setup
pygame.init()
screenHeight = 720
screenWidth = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True

lineLength = 600
lineWidth = 6
leftPadding = 240
topPadding = 80
#spaceOfLines = 50

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
    pygame.draw.rect(screen, pygame.Color(255,255,255), pygame.Rect((screenWidth-(leftPadding)), (0+(topPadding)), lineWidth, lineLength), 6)
    pygame.draw.rect(screen, pygame.Color(255,255,255), pygame.Rect((0+(leftPadding)), (0+(topPadding)), lineWidth, lineLength), 6)
    pygame.draw.rect(screen, pygame.Color(255,255,255), pygame.Rect(( (screenHeight/2) - (lineLength/2) ), (0+(leftPadding)), lineLength, lineWidth), 6)
    pygame.draw.rect(screen, pygame.Color(255,255,255), pygame.Rect(( (screenHeight/2) - (lineLength/2) ), (screenHeight-(leftPadding)), lineLength, lineWidth), 6)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()