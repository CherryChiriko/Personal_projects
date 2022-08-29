from sre_compile import isstring
import numpy as np
import string
import random
import keyboard

class Game:
    def __init__(self, dim):
        self.shots_left = 50   # shots to end the game
    pass


class Board:
    def __init__(self, dim):  # building the empty board
        self.dim = dim
        self.board = np.full((dim+1,dim+1), " ")
        self.ships_list = []    # ships already on the board
        self.ships_dimensions = [4,3] #[4,3,3,2,2,2,1,1,1,1]
        self.shots_left = 50

        for i, letter in enumerate(string.ascii_uppercase):  # write letters as board coordinates
            if i+1 == len(self.board[0]): break
            self.board[i+1][0] = letter
        for i in range(0,dim):                              # write numbers as board coordinates
            self.board[0][i+1] = str(i)

    def generate_board(self):
        i = 50
        while self.ships_dimensions:
            if not i: self.generete_board
            for dim in self.ships_dimensions:
                l = len(self.ships_list)
                while len(self.ships_list)== l:
                    self.place_ship_random(dim)
            i-=1
        
            
    
    def place_ship_random(self, dim):
        ship = Ship(dim)
        ship.set_elements(self)

        for ship_on_board in self.ships_list:
            ship_board = Ship(len(ship_on_board))
            ship_board.elements = ship_on_board
            ship_board.set_surr(self)
            print(ship_board.elements)
            for el in ship.elements:
                print(el)
                if el in ship_on_board or el in ship_board.surround: return

        self.ships_list.append(ship.elements)
        for el in ship.elements:
            el_x, el_y = el
            self.board[el_x][el_y]= 'o'
        ship.set_surr(self)
        for el in ship.surround:
            el_x, el_y = el
            self.board[el_x][el_y]= 'x'


    def place_ship_by_coordinates(self, coordinates):
        ship = Ship(len(coordinates))
        ship.elements = coordinates

        for ship_on_board in self.ships_list:
            ship_board = Ship(len(ship_on_board))
            ship_board.elements = ship_on_board
            ship_board.set_surr(self)
            print(ship_board.elements)
            for el in ship.elements:
                print(el)
                if el in ship_on_board or el in ship_board.surround: return

        self.ships_list.append(ship.elements)
        for el in ship.elements:
            el_x, el_y = el
            self.board[el_x][el_y]= 'o'
        ship.set_surr(self)
        for el in ship.surround:
            el_x, el_y = el
            self.board[el_x][el_y]= 'x'




class Ship:
    def __init__(self, dim):
        self.dim = dim
        self.elements = []
        self.surround = []
    
    def set_surr(self, board):
        x_points = [(1,0), (-1,0), (1,1),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1)]
        for el in self.elements:
            el_x, el_y = el
            for dx,dy in x_points:
                x = el_x + dx; y = el_y + dy
                if x > board.dim or y > board.dim or not x > 0 or not y > 0: continue
                else: 
                    surr = (x, y)
                    if surr in self.elements : continue
                    else : self.surround.append(surr)

    def set_elements(self, board):

        direction_switch = {0: (0, 1), 1: (1,0)}  #0: right, 1: down

        n = random.randint(0,1)
        dx, dy = direction_switch.get(n)

        r1, r2 = random.randint(1, board.dim),random.randint(1,board.dim-self.dim+1)
        x_i = r1 if not n else r2              #if down x in [1,10], y in [1,11-dim]; if right x in [1,11-dim], y in [1,10]
        y_i = r2 if not n else r1
        x_f = x_i + dx * (self.dim-1)
        y_f = y_i + dy * (self.dim-1)
        position_i = (x_i, y_i) 

        self.elements.append(position_i)
        if self.dim == 1: return self.elements
        
        for i in range(1, self.dim):
            x = x_i + i*dx; y = y_i + i*dy
            self.elements.append((x,y))
        print(self.elements)
        



b2 = Board(10)
b2.place_ship_by_coordinates([(4,3),(4,4)])
b2.place_ship_by_coordinates([(4,4),(4,5),(4,6)])
b2.place_ship_by_coordinates([(9,0),(9,1),(9,2)])  # use menu class to fix
b2.place_ship_random(4)
b2.place_ship_random(3)
print(b2.board)


#use counter to break while loop, recursive