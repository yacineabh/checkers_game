from const import *
from board import Board
from square import Square
from piece import Piece
from dragger import Dragger
import pygame 

class Game():
    def __init__(self) :
        self.board=Board()
        self.dragger=Dragger()
        self.player_turn='brown'
    
    def show_bg(self,screen):
        for row in range(rows):
            for col in range(cols):
                color=(255,255,255) if (row+col)%2==0 else (0,0,0)
                rect=(sqsize*col,sqsize*row,sqsize,sqsize)
                pygame.draw.rect(screen,color,rect)
        
    def show_pieces(self,screen):
        for row in range(rows):
            for col in range(cols):
                if self.board.squares[row][col].has_piece() and self.board.squares[row][col].piece!=self.dragger.piece :
                    piece=self.board.squares[row][col].piece
                    img=pygame.image.load(piece.texture)
                    piece.texture_rect=img.get_rect()
                    piece.texture_rect.center=(col*sqsize+sqsize//2,row*sqsize+sqsize//2)
                    screen.blit(img,piece.texture_rect)
                    
    
    def show_moves(self,screen):
        if self.dragger.piece!=None:
            color=(255, 120, 120)
            for move in self.dragger.piece.moves:
                rect=(move.final.col*sqsize,move.final.row*sqsize,sqsize,sqsize)
                pygame.draw.rect(screen,color,rect)
            
    def show_last_move(self,screen,last_move):
        if last_move!=None:
            initial=last_move.initial
            final=last_move.final
            rect1=(initial.col*sqsize,initial.row*sqsize,sqsize,sqsize)
            rect2=(final.col*sqsize,final.row*sqsize,sqsize,sqsize)
            color=(71, 169, 146)
            pygame.draw.rect(screen,color,rect1)
            pygame.draw.rect(screen,color,rect2)
        
    def update_player(self):
        if not(self.board.another_trun):
            self.player_turn='gray' if self.player_turn=='brown' else 'brown'
            self.board.killing_moves=[]
        else :
            self.board.another_trun=False