#Tic Tac Toe Cross

import  pygame

class Cross:
    
    screen = 0
    color = 0
    screen_width = 0
    screen_height = 0
    screen_padding = 0
    line_padding = 0
    line_width = 0
    cross_padding = 10
    cross_width = 40

    def __init__(self, screen, color, screen_width, screen_height, screen_padding, line_padding, line_width):
        self.screen = screen
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_padding = screen_padding
        self.line_padding = line_padding
        self.line_width = line_width

    def Draw(self):
        line_1_start_pos_x = 10
        line_1_start_pos_y = 10
        line_1_end_pos_x = line_1_start_pos_x + self.cross_width
        line_1_end_pos_y = line_1_start_pos_y + self.cross_width

        line_2_start_pos_x = line_1_start_pos_x
        line_2_start_pos_y = line_1_start_pos_y + self.cross_width
        line_2_end_pos_x = line_1_end_pos_x 
        line_2_end_pos_y = line_1_end_pos_y - 40

        #First Line
        pygame.draw.line(self.screen,self.color,(line_1_start_pos_x,line_1_start_pos_y),(line_1_end_pos_x,line_1_end_pos_y),self.line_width)

        #Second Line
        pygame.draw.line(self.screen,self.color,(line_2_start_pos_x,line_2_start_pos_y),(line_2_end_pos_x,line_2_end_pos_y),self.line_width)