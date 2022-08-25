from sre_compile import isstring
import numpy as np
import string
import random
import keyboard

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

    def update_board(self, coordinates, shot_type):
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
    h = board.shots_left
    shot_type = ''
    for i, ship in enumerate(board.ships_list):
        for element in board.ships_list[i]:
            if len(ship) == 1 and coordinates == element : 
                print("Hit and sunk!")
                board.shots_left -= 1; board.ships_list.remove(ship)
                shot_type = '#'; break
            if coordinates == element : 
                print("Hit!") 
                board.shots_left -= 1; ship.remove(element)
                shot_type = 'o'; break
    if h == board.shots_left : 
        print("Miss!"); board.shots_left -= 1
        shot_type = 'x'
    print("Shots left: ", board.shots_left)
    return coordinates, shot_type
    #board.update_board(board, coordinates)

   
playing = True
b1 = Board(10)
print("**** Welcome to the battleship game! ****")
print("The game board is 10x10 with rows ranging from 0 to 9 and columns from A to J\nIt is currently not possible to change the dimension of the board, but please stay tuned for updates.")
print("Press 'Ctrl+C' to exit at any time.")
print("****************************************")
try:
    while playing:
        print("You have a total of ", b1.shots_left, " shots.")
        print(b1.board)
        
        try: 
            coordinates = input("Type the coordinates of your shot in the following format: L0.\n")
            x, y = coordinates
        except ValueError: print("Input not valid"); continue
        x = x.upper()
        if x not in "ABCDEFGHIJ": print("Input not valid"); continue    # hard coded lol
            
        try: y = int(y)
        except: print("not valid"); continue

        for i, letter in enumerate(string.ascii_uppercase): 
            if x == letter: x = i+1
        coordinates = (x, y)
        b1.update_board(shot(b1, coordinates))
        break

except KeyboardInterrupt: pass
print(b1.board)
shot(b1, ('J',1))
shot(b1, ('J',2))
shot(b1, ('J',3))
shot(b1, ('J',4))
