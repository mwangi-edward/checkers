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
        BROWN_kings : int
            number of BROWN king pieces
        white_kings : int
            number of white king pieces
        white_left : int
            number of white pieces on the board
        BROWN_left : int
            number of BROWN pieces on the board
    """
    def __init__(self):
        """Assigns values to the parameters and Creates the board.
        Returns
        -------
            None       
        """
        self.board =[]
        self.brown_left = self.white_left = 12
        self.brown_kings = self.white_kings = 0
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
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.brown_kings +=1

    def get_piece(self, row, col):
        return self.board[row][col]

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
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def get_valid_moves(self, piece):
        moves={}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BROWN or piece.king:
            pass

        if piece.color == WHITE or piece.king:
            pass

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last=[]
        for r in range(start, stop, step):
            if left < 0:
                break
    
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        pass
