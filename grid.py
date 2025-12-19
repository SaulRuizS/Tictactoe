#Tic Tac Toe grid lines

import pygame

class Grid:

    screen = 0
    grid_color = 0
    padding = 0
    screen_width = 0
    screen_height = 0
    line_width = 0


    def __init__(self, screen, grid_color, padding, screen_width, screen_height, line_width):
        self.screen = screen
        self.grid_color = grid_color
        self.padding = padding
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.line_width = line_width

    def Draw(self):
        
        #TOP GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (0 + self.padding,0 + self.padding), (self.screen_width - self.padding, 0 + self.padding), self.line_width)

        #RIGHT GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (0 + self.padding,0 + self.padding), (0 + self.padding, self.screen_height-self.padding), self.line_width)

        #BOTTOM GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (0 + self.padding,self.screen_height - self.padding), (self.screen_width - self.padding, self.screen_height - self.padding), self.line_width)

        #LEFT GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (self.screen_width - self.padding,0 + self.padding), (self.screen_width - self.padding, self.screen_height - self.padding), self.line_width)


