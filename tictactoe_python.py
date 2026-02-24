# Example file showing a basic pygame "game loop"
#import os
import pygame
from grid import Grid
from cross import Cross
from circle import Circle

# pygame setup
pygame.init()
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

line_length = SCREEN_HEIGHT * 0.8
line_width = 10
screen_padding = 100 #(SCREEN_HEIGHT * 0.2) - (line_width/2)
grid_line_padding = 270
#leftPadding = 240
#top_padding = 60
#spaceOfLines = 50
circle_radius = ( ( (line_length / 3) - (line_width / 2) ) / 2 ) - (screen_padding * 0.2)
cross_width = (line_length / 3) - (line_width / 2) - (screen_padding * 0.7)

grid_color = pygame.Color(0,255,255)
cross_color = pygame.Color(200,100,200)
circle_color = pygame.Color(255,255,0)
#pygame.Color(0,255,255)
#pygame.Color(255,255,0)

grid = Grid(screen,grid_color,screen_padding,grid_line_padding,SCREEN_WIDTH,SCREEN_HEIGHT,line_width)

cross = Cross(screen,cross_color,SCREEN_WIDTH,SCREEN_HEIGHT,screen_padding,grid_line_padding,line_width,cross_width)

circle = Circle(screen,circle_color,SCREEN_WIDTH,SCREEN_HEIGHT,screen_padding - 190,grid_line_padding,circle_radius,line_width)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    grid.Draw()

    cross.Draw()

    circle.Draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()