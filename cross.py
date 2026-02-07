#Tic Tac Toe Cross

import  pygame

class Cross:
    
    screen = 0
    color = 0

    screen_width = 0
    screen_height = 0
    screen_padding = 0

    grid_line_padding = 0
    line_width = 0

    cross_padding = 10
    cross_width = 0
    cross_line_length = 0

    def __init__(self, screen, color, screen_width, screen_height, screen_padding, grid_line_padding, line_width, cross_width):
        self.screen = screen
        self.color = color

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_padding = screen_padding

        self.grid_line_padding = grid_line_padding
        self.line_width = line_width
        self.cross_width = cross_width

    def Draw(self):
        line_1_start_pos_x = self.grid_line_padding - self.screen_padding - (self.cross_width / 2)
        line_1_start_pos_y = self.grid_line_padding - self.screen_padding - (self.cross_width / 2)
        line_1_end_pos_x = line_1_start_pos_x + self.cross_width
        line_1_end_pos_y = line_1_start_pos_y + self.cross_width

        line_2_start_pos_x = line_1_start_pos_x
        line_2_start_pos_y = line_1_start_pos_y + (self.cross_width / 2)
        line_2_end_pos_x = line_1_end_pos_x 
        line_2_end_pos_y = line_1_end_pos_y - (self.cross_width / 2)

        #First Line
        pygame.draw.line(self.screen,self.color,(line_1_start_pos_x,line_1_start_pos_y),(line_1_end_pos_x,line_1_end_pos_y),self.line_width)

        #Second Line
        pygame.draw.line(self.screen,self.color,(line_2_start_pos_x,line_2_start_pos_y),(line_2_end_pos_x,line_2_end_pos_y),self.line_width)