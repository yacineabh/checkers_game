import os
import pygame

class Piece():
    def __init__(self,name,color,texture=None,texture_rect=None) :
        self.name=name
        self.color=color
        self.moves=[]
        self.killing_moves=[]
        self.set_texture()
        self.texture_rect=texture_rect
        self.kill=False
        
        
    def set_texture(self):
        self.texture=os.path.join(f'{self.color}_{self.name}.png')
        
    def add_move(self,move):
        self.moves.append(move)
        
    
class Normal(Piece):
    def __init__(self,color):
        self.dir=-1 if color=='brown' else 1
        super().__init__('normal',color)
        
class King(Piece):
    def __init__(self,color):
        super().__init__('king',color)


