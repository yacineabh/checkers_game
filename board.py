from const import *
from square import Square
from piece import *
from move import Move
class Board():
    def __init__(self) :
        self.squares=[[0,0,0,0,0,0,0,0] for row in range(rows)]
        self.create()
        self.add_piece('brown')
        self.add_piece('gray')
        self.killing_moves=[]
        self.another_trun=False
        self.killed_pieces=[]
        self.last_move=None
        
    
    def calc_moves(self,row,col,piece):
        
        
        def normal_moves():
            piece.kill=False
            possible_moves=[(row+piece.dir,col+1),(row+piece.dir,col-1)]
            for possible_move in possible_moves:
                row_move=possible_move[0]
                col_move=possible_move[1]
                if Square.in_range(row_move,col_move):
                    if self.squares[row_move][col_move].is_empty():
                        initial=Square(row,col)
                        final=Square(row_move,col_move)
                        move=Move(initial,final)
                        piece.add_move(move)
                    elif self.squares[row_move][col_move].has_enemy_piece(piece.color):
                        # self.save_killed_piece(row_move,col_move)
                        row_move+=piece.dir
                        col_move+=col_move-col
                        if Square.in_range(row_move,col_move):
                            if self.squares[row_move][col_move].is_empty():
                                initial=Square(row,col)
                                final=Square(row_move,col_move)
                                move=Move(initial,final)
                                piece.add_move(move)
                                piece.kill=True
                                self.killing_moves.append(move)
                                piece.killing_moves.append(move)
                                #break
                                
        def king_moves():
            piece.kill=False
            
            dirs=[(1,1),(1,-1),(-1,-1),(-1,1)]
            
            for dir in dirs:
                row_dir=dir[0]
                col_dir=dir[1]
                out=False
                
                row_move=row+row_dir
                col_move=col+col_dir
                while True:
                    if Square.in_range(row_move,col_move):
                        if self.squares[row_move][col_move].is_empty():
                            initial=Square(row,col)
                            final=Square(row_move,col_move)
                            move=Move(initial,final)
                            piece.add_move(move)
                           
                            row_move+=row_dir
                            col_move+=col_dir
                        elif out:
                            break
                        elif self.squares[row_move][col_move].has_enemy_piece(piece.color):
                            out=True
                           # if len(self.killed_pieces)<5:
                                
                            self.save_killed_pieces(row_move,col_move)
                            print(self.killed_pieces)
                            while True:
                                row_move+=row_dir
                                col_move+=col_dir
                                
                                if Square.in_range(row_move,col_move):
                                    if self.squares[row_move][col_move].is_empty():
                                        initial=Square(row,col)
                                        final=Square(row_move,col_move)
                                        move=Move(initial,final)
                                        piece.add_move(move)
                                        self.killing_moves.append(move)
                                        piece.killing_moves.append(move)
                                        piece.kill=True
                                    else :
                                        break
                                else:
                                    break
                        else:
                            break
                    else:
                        break
                                        
                        
        
        
        
        if isinstance(piece,Normal):
            normal_moves()
        elif isinstance(piece,King):
            king_moves()
    
    def find_the_piece(self,move,place):
        f=move.final
        i=move.initial
        px=place[1]
        py=place[0]
        if f.col>i.col and f.row>i.row :
            return i.col<px<f.col and i.row<py<f.row
        elif f.col>i.col and f.row <i.row:
            return i.col<px<f.col and f.row<py<i.row
        elif f.col<i.col and f.row <i.row:
            return f.row<py<i.row and f.col<px<i.col
        elif f.col<i.col and f.row>i.row:
            return i.row<py<f.row and f.col<px<i.col
    
    def save_killed_piece(self,row,col):
        self.killed_row=row
        self.killed_col=col
    
    def save_killed_pieces(self,row,col):
        self.killed_pieces.append((row,col))    
    
    def kill_piece(self,row,col):
        self.squares[row][col].piece=None
    
    
    def  check_promotion(self,row):
        return row==7 or row==0
         
    
    def move(self,piece,move):
        self.squares[move.initial.row][move.initial.col].piece=None
        self.squares[move.final.row][move.final.col].piece=piece
        piece.moves=[]
        piece.killing_moves=[]
        self.last_move=Move(move.initial,move.final)
       
        
        if piece.kill and piece.name=='normal':
            self.kill_piece(move.initial.row+piece.dir,move.initial.col+(move.final.col-move.initial.col)//2)
            if not(self.check_promotion(move.final.row)):
                self.calc_moves(move.final.row,move.final.col,piece)
                '''
                if self.check_promotion(move.final.row):
                    self.squares[move.final.row][move.final.col].piece=King(piece.color)
                    piece= self.squares[move.final.row][move.final.col].piece
                    self.calc_moves(move.final.row,move.final.col,piece)
                '''   
                if piece.kill:
                    self.another_trun=True
                
    
    
        if piece.name=='normal' and self.check_promotion(move.final.row):
            self.squares[move.final.row][move.final.col].piece=King(piece.color)
            if piece.kill:
                piece=self.squares[move.final.row][move.final.col].piece
                self.calc_moves(move.final.row,move.final.col,piece)
                print('bellow')
                print(piece.killing_moves)
                if piece.killing_moves!=[]:
                    self.another_trun=True
                    
                
              
                
            
            
        
        elif piece.kill and piece.name=='king':
            
            for place in self.killed_pieces:
                print('this is what we are looking for')
                print(place[0],place[1])
                
                if self.find_the_piece(move,place):
                    self.save_killed_piece(place[0],place[1])
                    print('good')
                    self.killed_pieces=[]
                    break
            self.kill_piece(self.killed_row,self.killed_col)
            self.calc_moves(move.final.row,move.final.col,piece)
            if piece.kill:
                self.another_trun=True
        self.killed_pieces=[]
                       
            
        
    def valid_move(self,piece,move):
        for m in piece.moves:
            if move.eq(m):
                return True
        return False
    
    def find_killing_moves(self,color):
        for row in range(rows):
            for col in range(cols):
                if self.squares[row][col].has_team_piece(color):
                    piece= self.squares[row][col].piece
                    self.calc_moves(row,col,piece)
                    piece.moves=[]
        self.killed_pieces=[]
    
               
    
    def free_move(self):
        return (self.killing_moves==[])                  
    
    def create(self):
         for row in range(rows):
            for col in range(cols):
                self.squares[row][col]=Square(row,col)
    
    def add_piece(self,color):
        put_in_black= (color=='gray')
        init_rows=[0,1,2] if put_in_black else [5,6,7]
        
        for row in init_rows:
            for col in range(cols):
                if (row+col)%2==1 :
                    self.squares[row][col]=Square(row,col,Normal(color))
        
        
        
        