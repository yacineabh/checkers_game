from square import Square




def find_the_piece(self,move,place): 
    f=move.final
    i=move.initial
    px=place[1]
    py=place[0]
    if f.col>i.col and f.row>i.col :
        return i.col<px<f.col and i.row<py<f.row
    elif f.col>i.col and f.row <i.col:
        return i.col<px<f and f.row<py<i.row
    elif f.col<i.col and f.row <i.col:
        return f.row<py<i.row and f.col<px<i.col
    elif f.col<i.col and f.row>i.row:
        return i.row<py<f.row and f.col<px<i.col
        
