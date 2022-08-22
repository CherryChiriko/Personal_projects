import numpy as np
import string
import random

class Board:
    def __init__(self, dim):
        self.dim = dim
        # self.board = np.zeros((dim+1,dim+1), dtype=str)
        self.board = np.full((dim+1,dim+1), " ")

        for i, letter in enumerate(string.ascii_uppercase):
            if i+1 == len(self.board[0]): break
            self.board[0][i+1] = letter
        for i in range(1,dim+1):
            self.board[i][0] = str(i)
    
    def place_ship(self):
        ship = Ship(2, self)
        ship.get_ship_elements(self)
        x_points = [(1,0), (-1,0), (1,1),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1)]
        for el in ship.ship_elements:
            el_x, el_y = el
            self.board[el_x][el_y] = "o"

            for dx,dy in x_points:
                x = el_x + dx; y = el_y + dy
                print(x,y)
                if x> self.dim or y>self.dim : continue
                if self.board[x][y] != "o" and x>0 and y>0 : self.board[x][y] = "x"
    
    
        
class Ship:
    def __init__(self, dim, board):
        self.dim = dim
        self.position_i = (random.randint(1, board.dim),random.randint(1,board.dim))
        self.ship_elements = []

    def direction(self, n):
        direction_switch = {1: (-1,0), 2: (1,0), 3: (0,-1), 4:(0,1)}  #1: left, 2: right, 3: down, 4: up
        self.direc = direction_switch.get(n)

    def set_position_f(self):
        n = random.randint(1,4)
        self.direction(n)

        x_i, y_i = self.position_i
        x,y = self.direc
        x *= (self.dim-1); y*= (self.dim-1)
        x_f = x + x_i; y_f = y + y_i;
        if x_f > 0 and y_f >0 : self.position_f = (x_f, y_f)
        else: self.position_f = (x_i - x, y_i - y)   #temporary solution, it is not completely random if we do it in this way

        # self.position_f = tuple(map(lambda t : t[0]*self.dim + t[1], zip(self.direction(n), self.position_i)))
        #self.position_f = tuple(map(lambda a,b : a*self.dim + b, self.direc, self.position_i))
    
    def get_ship_elements(self, board):
        self.ship_elements.append(self.position_i)
        if self.dim == 1: return self.ship_elements
        self.set_position_f()
        for i in range(1, self.dim):
            dx, dy = self.direc
            x_i, y_i = self.position_i
            x = x_i + i*dx; y = y_i + i*dy
            self.ship_elements.append((x,y))
            print(self.ship_elements)
        self.move_elements(board)

    def move_elements(self, board): 
        for i, el in enumerate(self.ship_elements):
            x, y = el
            x_i, y_i = self.position_i
            if x> board.dim or y> board.dim or x<0 or y<0 or board.board[x][y] in ["x","o"]: 
                x1, y1 = self.ship_elements[-2]
                x2, y2 = self.ship_elements[-1]
                dx, dy = (x2-x1, y2-y1)
                if (x2 + dx)> board.dim or (y2 + dy)> board.dim or (x2 + dx)<0 or (y2 + dy)<0 or board.board[(x2 + dx)][(y2 + dy)] in ["x","o"]:
                    self.ship_elements[i] = (x_i - dx, y_i -dy)
                else:
                    self.ship_elements[i] = (x2 + dx, y2 +dy)
                print(self.ship_elements[i])
                print("I'm moving ", el, "to ", self.ship_elements[i])
        



b1 = Board(10)
b1.place_ship()
print(b1.board)


