import pygame

class Dragger():
    def __init__(self):
        self.piece=None
        self.dragging=False
        self.mouseX=0
        self.mouseY=0
        self.initial_row=0
        self.initial_col=0
        
    def update_mouse(self,pos):
        self.mouseX=pos[0]
        self.mouseY=pos[1]
        
    def update_blit(self,screen):
        if self.piece!=None:
            img=pygame.image.load(self.piece.texture)
            rect=img.get_rect()
            rect.center=(self.mouseX,self.mouseY)
            screen.blit(img,rect)
        
    
    def drag(self,piece):
        self.dragging=True
        self.piece=piece
        
    def undrag(self):
        self.piece.moves=[]
        self.piece.killing_moves=[]
        self.dragging=False
        self.piece=None
        