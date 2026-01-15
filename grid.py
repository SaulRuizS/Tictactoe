#Tic Tac Toe grid lines

import pygame

class Grid:

    screen = 0
    grid_color = 0
    screen_padding = 0
    line_padding = 0
    screen_width = 0
    screen_height = 0
    line_width = 0


    def __init__(self, screen, grid_color, screen_padding, line_padding, screen_width, screen_height, line_width):
        self.screen = screen
        self.grid_color = grid_color
        self.screen_padding = screen_padding
        self.line_padding = line_padding
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.line_width = line_width

    def Draw(self):
        
        #TOP GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (self.screen_padding,self.line_padding), (self.screen_width - self.screen_padding,self.line_padding), self.line_width)

        #LEFT GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (self.line_padding,self.screen_padding), (self.line_padding, self.screen_height-self.screen_padding), self.line_width)

        #BOTTOM GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (self.screen_padding,self.screen_height - self.line_padding), (self.screen_width - self.screen_padding, self.screen_height - self.line_padding), self.line_width)

        #RIGHT GRID LINE
        pygame.draw.line(self.screen, self.grid_color, (self.screen_width - self.line_padding,self.screen_padding), (self.screen_width - self.line_padding, self.screen_height - self.screen_padding), self.line_width)


