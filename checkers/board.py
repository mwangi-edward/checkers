import pygame
from .constants import BLACK, WHITE, COLS, ROWS, SQUARE_SIZE, BROWN
from .piece import Piece
class Board:
    """
    A class to draw/create a checkers Board
    
    Attributes
    ----------
        board : list
            board number of squares on the board
        red_kings : int
            number of red king pieces
        white_kings : int
            number of white king pieces
        white_left : int
            number of white pieces on the board
        red_left : int
            number of red pieces on the board
    """
    def __init__(self):
        """Assigns values to the parameters and Creates the board.
        Returns
        -------
            None       
        """
        self.board =[]
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kigs = 0
        self.create_board()

    def draw_squares(self,win):
        """
        Draws the checkers board on the window generated.

        Parameters
        ----------
            win : object
                Contains a blank window
        Returns
        -------
            None 
        """
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE,(row*SQUARE_SIZE, col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE) )
    def create_board(self):
        """
        Creates the board as per the attributes assigned
        """
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 ==((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BROWN))
                    else :
                        self.board[row].append(0)                        
                else:
                    self.board[row].append(0)

    def draw(self,win):
        """
        Draws the pieces on the board by calling using the class Piece (piece.draw)

        Parameters
        ----------
            win : Object
                Current window after board has been drawn
        """
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece= self.board[row][col]
                if piece != 0:
                    piece.draw(win)
