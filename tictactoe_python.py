# Example file showing a basic pygame "game loop"
#import os
import pygame
from grid import Grid

# pygame setup
pygame.init()
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

line_length = SCREEN_HEIGHT * 0.8
line_width = 10
padding = (SCREEN_HEIGHT * 0.2) - (line_width/2)
#leftPadding = 240
#top_padding = 60
#spaceOfLines = 50

grid_color = pygame.Color(255,255,255)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    #TOP GRID LINE
    pygame.draw.line(screen, grid_color,(0+padding,0+padding), (SCREEN_WIDTH-padding, 0+padding), line_width)

    #RIGHT GRID LINE
    pygame.draw.line(screen, pygame.Color(255,0,255),(0+padding,0+padding), (0+padding, SCREEN_HEIGHT-padding), line_width)

    #BOTTOM GRID LINE
    pygame.draw.line(screen, pygame.Color(0,255,255),(0+padding,SCREEN_HEIGHT-padding), (SCREEN_WIDTH-padding, SCREEN_HEIGHT-padding), line_width)

    #LEFT GRID LINE
    pygame.draw.line(screen, pygame.Color(255,255,0),(SCREEN_WIDTH-padding,0+padding), (SCREEN_WIDTH-padding, SCREEN_HEIGHT-padding), line_width)

    #LEFT GRID LINE
    #pygame.draw.rect(screen, grid_color, pygame.Rect((0+(padding)), (0+(padding)), line_width, line_length), 6)
    
    #RIGHT GRID LINE
    #pygame.draw.rect(screen, grid_color, pygame.Rect((SCREEN_WIDTH-(padding)), (0+(padding)), line_width, line_length), 6)

    #TOP GRID LINE
    #pygame.draw.rect(screen, grid_color, pygame.Rect(( (SCREEN_HEIGHT/2) - (line_length/2) ), (0+(padding)), line_length, line_width), 6)
    
    #BOTTOM GRID LINE
    #pygame.draw.rect(screen, grid_color, pygame.Rect(( (SCREEN_HEIGHT/2) - (line_length/2) ), (SCREEN_HEIGHT-(padding)), line_length, line_width), 6)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()