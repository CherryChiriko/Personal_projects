import numpy as np
import string
import random

class Board:
    def __init__(self, dim):  # building the basic board
        self.dim = dim
        self.board = np.full((dim+1,dim+1), " ")
        self.ships_list = [[(4,3),(4,4)],[(10,1), (10,2),(10,3)]]
        self.shots_left = 50

        for i, letter in enumerate(string.ascii_uppercase):
            if i+1 == len(self.board[0]): break
            self.board[0][i+1] = letter
        for i in range(1,dim+1):
            self.board[i][0] = str(i)
        print(self.board)
    
    
    def place_ship(self):
        ships = [4,3]
        while ships:
            ship = Ship(ships[0])
            l = len(ships)
            #elements, surr = ship.set_ship_elements(self)
            elements = [(4,3)]
            if el in self.ship: ships = [ships[0]] + ships; break
            ships.pop(0)
            if len(ships) != l: self.ship.append(elements)
            print(self.ship)

    def update_board(self, coordinates):
        x, y = coordinates
        self.board[x][y] = "x"
        print(self.board)



class Ship:
    def __init__(self, dim):
        self.dim = dim

    def set_ship_elements(self, board):
        ship_elements = []
        ship_surround = []

        x_points = [(1,0), (-1,0), (1,1),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1)]
        direction_switch = {0: (0, 1), 1: (1,0)}  #0: right, 1: down

        n = random.randint(0,1)
        dx, dy = direction_switch.get(n)

        r1, r2 = random.randint(1, board.dim),random.randint(1,board.dim-self.dim+1)
        x_i = r1 if not n else r2              #if down x in [1,10], y in [1,11-dim]; if right x in [1,11-dim], y in [1,10]
        y_i = r2 if not n else r1
        x_f = x_i + dx * (self.dim-1)
        y_f = y_i + dy * (self.dim-1)
        position_i = (x_i, y_i) 

        ship_elements.append(position_i)
        if self.dim == 1: return ship_elements
        
        for i in range(1, self.dim):
            x = x_i + i*dx; y = y_i + i*dy
            ship_elements.append((x,y))
        print(ship_elements)
        for element in ship_elements:
            el_x, el_y = element
            for dx,dy in x_points:
                x = el_x + dx; y = el_y + dy
                if x> board.dim or y>board.dim or not x>0 or not y>0: continue
                else: 
                    surr= (x, y)
                    if surr in ship_elements : continue
                    else : ship_surround.append(surr)
        return ship_elements, ship_surround
        

def shot (board, coordinates):
    x, y = coordinates
    x = x.upper()
    for i, letter in enumerate(string.ascii_uppercase): 
        if x == letter: x = i+1
    coordinates = (x, y)
    h = board.shots_left
    for i, ship in enumerate(board.ships_list):
        for element in board.ships_list[i]:
            if len(ship) == 1 and coordinates == element : print("Hit and sunk!"); board.shots_left -= 1; board.ships_list.remove(ship); break
            if coordinates == element : print("Hit!"); board.shots_left -= 1; ship.remove(element); break
    if h == board.shots_left : print("Miss!"); board.shots_left -= 1
    print("Shots left: ", board.shots_left)
    #board.update_board(board, coordinates)
            

b1 = Board(10)
#print(b1.board)
shot(b1, ('J',1))
shot(b1, ('J',2))
shot(b1, ('J',3))
shot(b1, ('J',4))


