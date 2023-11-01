import pygame
from const import *
from game import Game
from square import Square
from move import Move


class Main():
    def __init__(self) :
        self.screen=pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('demma')
        self.game=Game()
        
    def mainloop(self):
        
        run=True
        screen=self.screen
        game=self.game
        board=game.board
        dragger=self.game.dragger
        
        while run:
            game.show_bg(screen)
            game.show_last_move(screen,board.last_move)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.update_mouse(event.pos)
                game.show_moves(screen)
                dragger.update_blit(screen)
            else:
                board.find_killing_moves(game.player_turn)
                    
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row=int(dragger.mouseY//sqsize)
                    clicked_col=int(dragger.mouseX//sqsize)
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece=board.squares[clicked_row][clicked_col].piece
                        
                        if game.player_turn==piece.color:
                            dragger.drag(piece)
                            if board.free_move():
                               
                                board.calc_moves(clicked_row,clicked_col,piece)
                            else :
                                piece.moves=piece.killing_moves
                        
                elif event.type==pygame.MOUSEMOTION:
                    if dragger.dragging:
                        game.show_bg(screen)
                        game.show_last_move(screen,board.last_move)
                        dragger.update_mouse(event.pos)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        
                        dragger.update_blit(screen)
                    
                elif event.type==pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row=int(dragger.mouseY//sqsize)
                        released_col=int(dragger.mouseX//sqsize)
                        initial=Square(clicked_row,clicked_col)
                        final=Square(released_row,released_col)
                        move=Move(initial,final)
                        if board.valid_move(dragger.piece,move):
                            board.calc_moves(clicked_row,clicked_col,piece)
                            board.move(dragger.piece,move)
                            game.update_player()
                            
                                
                        dragger.undrag()   
                     
                
                elif event.type==pygame.QUIT:
                    run=False
                    
            pygame.display.update()

main=Main()
main.mainloop()

        