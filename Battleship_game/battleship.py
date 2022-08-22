import numpy as np
import string
import random

class Board:
    def __init__(self, dim):  # building the basic board
        self.dim = dim
        self.board = np.full((dim+1,dim+1), " ")

        for i, letter in enumerate(string.ascii_uppercase):
            if i+1 == len(self.board[0]): break
            self.board[0][i+1] = letter
        for i in range(1,dim+1):
            self.board[i][0] = str(i)
    
    def place_ship(self):
        ship = Ship(4)
        elements = ship.set_ship_elements(self)
        x_points = [(1,0), (-1,0), (1,1),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1)]
        for el in elements:
            el_x, el_y = el
            self.board[el_x][el_y] = "o"

            for dx,dy in x_points:
                x = el_x + dx; y = el_y + dy
                if x> self.dim or y>self.dim : continue
                if self.board[x][y] != "o" and x>0 and y>0 : self.board[x][y] = "x"
    
    
        
class Ship:
    def __init__(self, dim):
        self.dim = dim

    def set_ship_elements(self, board):
        ship_elements = []

        direction_switch = {0: (0, 1), 1: (1,0)}  #0: right, 1: down
        n = random.randint(0,1)
        dx, dy = direction_switch.get(n)
        r1, r2 = random.randint(1, board.dim),random.randint(1,board.dim-self.dim+1)
        x_i = r1 if not n else r2                    #if down x in [1,10], y in [1,11-dim]; if right x in [1,11-dim], y in [1,10]
        y_i = r2 if not n else r1
        x_f = x_i + dx * (self.dim-1)
        y_f = y_i + dy * (self.dim-1)
        position_i = (x_i, y_i) 
        print("(",x_i, ",",y_i,")","(",x_f, ",",y_f,")")

        ship_elements.append(position_i)
        if self.dim == 1: return ship_elements
        
        for i in range(1, self.dim):
            x = x_i + i*dx; y = y_i + i*dy
            ship_elements.append((x,y))
            print(ship_elements)
        return ship_elements
        



b1 = Board(10)
b1.place_ship()
print(b1.board)


