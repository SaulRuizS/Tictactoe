#Tic Tac Toe Circle

import  pygame

class Circle:
    
    screen = 0
    color = 0
    screen_width = 0
    screen_height = 0
    screen_padding = 0
    line_padding = 0
    line_width = 0
    circle_padding = 40
    circle_width = 40

    def __init__(self, screen, color, screen_width, screen_height, screen_padding, line_padding, line_width):
        self.screen = screen
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_padding = screen_padding
        self.line_padding = line_padding
        self.line_width = line_width

    def Draw(self):
        line_1_start_pos_x = self.circle_padding
        line_1_start_pos_y = self.circle_padding
        line_1_end_pos_x = line_1_start_pos_x + self.circle_width
        line_1_end_pos_y = line_1_start_pos_y + self.circle_width

        line_2_start_pos_x = line_1_start_pos_x
        line_2_start_pos_y = line_1_start_pos_y + self.circle_width
        line_2_end_pos_x = line_1_end_pos_x 
        line_2_end_pos_y = line_1_end_pos_y - self.circle_width

        #
        pygame.draw.circle(self.screen,self.color,(line_1_start_pos_x,line_1_start_pos_y),self.circle_padding,self.line_width)