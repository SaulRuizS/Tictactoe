#Tic Tac Toe Circle

import  pygame

class Circle:
    
    screen = 0
    color = 0

    screen_width = 0
    screen_height = 0
    screen_padding = 0
    
    circle_pos_padding = 0
    circle_line_width = 0
    circle_radius = 0

    def __init__(self, screen, color, circle_radius, line_width):
        self.screen = screen
        self.color = color

        self.circle_radius = circle_radius
        self.circle_line_width = line_width

    def Draw(self, screen_width, screen_height, screen_padding, grid_line_padding,):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_padding = screen_padding
        
        self.circle_pos_padding = grid_line_padding - self.screen_padding

        circle_start_pos_x = self.circle_pos_padding
        circle_start_pos_y = self.circle_pos_padding

        pygame.draw.circle(self.screen,self.color,(circle_start_pos_x,circle_start_pos_y),self.circle_radius,self.circle_line_width)