 
 
class Move():
    def __init__(self,initial,final):
        #initial and final are Squares
        self.initial=initial
        self.final=final

    def eq(self,move):
        return self.initial.row==move.initial.row and self.initial.col==move.initial.col \
               and self.final.row==move.final.row and self.final.col==move.final.col
        