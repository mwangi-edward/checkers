import pygame
from .constants import RED,GREY, SQUARE_SIZE
class Piece:
    """
    A Class to draw pieces, assign piece positions and assign kings.
    
    Attributes
    ----------
        row : int
            row number(row position)
        col : int
            column number(column position)
        color : String 
            colour of the piece
        King: Bolean
            If the piece is a King or has been Kinged
        x : int
            position on the x axis
        y : int
            position on the y axis
        
    """
    PADDING = 10
    OUTLINE = 2
    def __init__(self, row, col, color):
        """
        On initiation assign the row, column position and colour for the pieces

        Parameters
        ----------

            row : integer
                row position on the board
            col : integer
                column position on the board            
            color : string
                Colour to be assigned to the piece           
        """
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x_axis = 0
        self.y_axis = 0
        self.calc_pos()
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

    def calc_pos(self):
        """
        Calcultes the center of a square on the board. 
        """
        self.x_axis = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 # SQUARE_SIZE // 2 == 37
        self.y_axis = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """
        Makes a piece a King
        """
        self.king = True

    def draw(self, win):
        """
        Draws the pieces on the board 

        Parameters
        ----------
            win : Object
                Generated window
        """
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x_axis,self.y_axis), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x_axis,self.y_axis), radius)
    
    def __repr__(self) -> str:
        return f'position = {(self.x_axis,self.y_axis)}\n'