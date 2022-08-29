# from sre_compile import isstring
#  isinstance(variable, str)
import numpy as np
import string
import random
#import keyboard

# alt+1+5  ☼

WHITESPACE = '⚫' #⚪🔵
BARCO = '🐱' #'🐶'
EQUIS = WHITESPACE
# EQUIS = '❌'
TRY_N_TIMES = 10

class Game:
    def __init__(self, dim):
        self.shots_left = 50   # shots to end the game
        self.style = ['emoji', 'traditional']
        self.players = 1
        self.board_dimension = 10
        self.ships_dimensions = [4,3,3,2,2,2,1,1,1,1]

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
    return shot_type
    #board.update_board(board, coordinates)

    b2 = Board(10)
b2.generate_board()
# b1 = Board(10)
# print("**** Welcome to the battleship game! ****")
# print("The game board is 10x10 with rows ranging from 0 to 9 and columns from A to J\nIt is currently not possible to change the dimension of the board, but please stay tuned for updates.")
# print("Press 'Ctrl+C' to exit at any time.")
# print("****************************************")
# print(b1.board)
# print("****************************************")
# try:
#     while b1.shots_left:
#         if not b1.ships_list : break
#         print("You have a total of ", b1.shots_left, " shots.")
        
#         try: 
#             coordinates = input("Type the coordinates of your shot in the following format: L0.\n")
#             x, y = coordinates
#         except ValueError: print("Input not valid"); continue
#         x = x.upper()
#         if x not in "ABCDEFGHIJ": print("Input not valid"); continue    # hard coded lol
            
#         try: y = int(y)+1
#         except: print("not valid"); continue

#         if y < 1 or y > 9 : print("not valid"); continue

#         for i, letter in enumerate("ABCDEFGHIJ"):   # string.ascii_uppercase): 
#             if x == letter: x = i+1

#         b1.update_board((x, y), shot(b1, (x, y)))

# except KeyboardInterrupt: pass
# print("**** GAME OVER! ****")
# if not b1.ships_list : print("°°°°  You won! °°°°")
# else: print("You lost!")
# print(b1.board)

class Board:
    def __init__(self, dim):  # building the empty board
        self.dim = dim
        self.board = np.full((dim+1,dim+1), WHITESPACE)
        self.ships_list = []    # ships already on the board
        # self.ships_dimensions = [4,3] #[4,3,3,2,2,2,1,1,1,1]
        self.ships_dimensions = [4,3,3,2,2,2,1,1,1,1]
        self.shots_left = 50

        for i, letter in enumerate(string.ascii_uppercase):  # write letters as board coordinates
            if i+1 == len(self.board[0]): break
            self.board[i+1][0] = letter
        for i in range(0,dim):                              # write numbers as board coordinates
            self.board[0][i+1] = str(i)

    def generate_board(self):
        while len(self.ships_list) != len(self.ships_dimensions):
            self.ships_list.clear()
        
            for dim in self.ships_dimensions:
                for _ in range(TRY_N_TIMES):
                    ship_placed = self.place_ship_random(dim)
                    if ship_placed: break

                if not ship_placed:
                    break
            
    
    def place_ship_random(self, dim):
        ship = Ship(dim)
        ship.set_elements(self)

        for ship_on_board in self.ships_list:
            ship_board = Ship(len(ship_on_board))
            ship_board.elements = ship_on_board
            ship_board.set_surr(self)
            for el in ship.elements:
                if el in ship_on_board or el in ship_board.surround: return False

        self.ships_list.append(ship.elements)
        for el in ship.elements:
            el_x, el_y = el
            self.board[el_x][el_y]= BARCO
        ship.set_surr(self)
        for el in ship.surround:
            el_x, el_y = el
            self.board[el_x][el_y]= EQUIS

        return True


    def place_ship_by_coordinates(self, coordinates):
        # check that coordinates are allowed
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
            self.board[el_x][el_y]= BARCO
        ship.set_surr(self)
        for el in ship.surround:
            el_x, el_y = el
            self.board[el_x][el_y]= EQUIS


    def update_board(self, coordinates, shot_type):
        x, y = coordinates
        self.board[x][y] = shot_type
        print(self.board)

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
b2.generate_board()
print(b2.board)

# >>> "o".isdigit()
# False
# >>> "o".isalpha()
# True