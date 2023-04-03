import numpy as np
import string
import random

TRY_N_TIMES = 10
# MAX_BOARD_DIM  = len(string.ascii_uppercase)
MAX_BOARD_DIM = 10
AVAILABLE_SHOTS = 50

EMPTY = 0
WATER = 1
SUNK = 2
FIRST_SHIP = 3

REVEAL = 1

DOGGS = "U・ᴥ・U"

def fill_submatrix(matrix, x0, x1, y0, y1, surrounding_value):
    matrix[max(0, x0-1) : x1 + 2, max(0, y0-1) : y1 + 2] = surrounding_value 


class Game:
    def __init__(self, dim, style):
        dim = min(MAX_BOARD_DIM, dim)
        self.input_letter_to_num = {char : i for i,char in enumerate(string.ascii_uppercase[:dim])}

        self.shots_left = AVAILABLE_SHOTS   # shots to end the game
        self.solution = Board(dim)
        self.mask = np.zeros((dim, dim), dtype = np.uint8)
        self.mask_reveal = np.ones((dim, dim), dtype = np.uint8)
        self.last_shot = ()

        self.style : dict
      
        self.set_style(style)

    def display_intro(self):                 
        self.print_board(self.mask_reveal)
        print("**** Welcome to the battleship game! ****")
        # print("The game board is 10x10 with rows ranging from 0 to 9 and columns from A to J\nIt is currently not possible to change the dimension of the board, but please stay tuned for updates.")
        print("Press 'Ctrl+C' to exit at any time.")
        print("****************************************")  
        
        self.solution.board[self.solution.board == 0] = 1 # temp

        self.print_board()
        print("****************************************")
        

    def shot (self, coordinates): 
        self.shots_left -= 1   # a shot will be counted if you hit a spot you have already tried, ammo is not free, don't waste it!

        if self.mask[coordinates]: print("You already shot here"); return

        self.mask[coordinates] = True
        self.last_shot = coordinates

        tile = self.solution.board[coordinates]
        if tile >= FIRST_SHIP:
            ship_sunk = self.solution.reduce_ship_HP(tile)

            if ship_sunk:
                self.solution.board[self.solution.board == tile] = SUNK
                ship_id = tile - FIRST_SHIP
                fill_submatrix(self.mask, *self.solution.ships_coordinates[ship_id], REVEAL)
                

        self.print_board()


    def set_style(self, new_style):
        # alternative emojis '⚪''🐱''🐶'   
        # https://emojiterra.com/transport-water/
        if new_style == 'emoji':
            self.style = {
                "tiles" : ['⚫', '🔵', '❌'] + ['🚢'] * len(self.solution.ships_dimensions),
                # "tiles" : ['⚫', '🔵', '❌'] + ['🚢', '🚤'] * (len(self.solution.ships_dimensions) // 2),
                # "tiles" : ['⚫', '🔵', '❌'] + ['🚢'] * 6 + ['🛶'] * 4,
                "numbers" : ['1️⃣ ','2️⃣ ','3️⃣ ','4️⃣ ','5️⃣ ','6️⃣ ','7️⃣ ','8️⃣ ','9️⃣ ','🔟 '],
                "letters" : [ '🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯'], #🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙
                "sep" : '  '
                }

        elif new_style == 'traditional':
            self.style = {
                "tiles" : ['.', '~', 'x'] + ['0'] * len(self.solution.ships_dimensions),
                "numbers" : [i for i in range(1, self.dim+1)],
                "letters" : string.ascii_uppercase[: self.dim],
                "sep" : ' '
                }
                 

    def gameplay(self):
        while self.shots_left:
            no_ships_left = not (self.solution.board >= FIRST_SHIP).any()
            
            if no_ships_left: break

            print(f">>> You have a total of {self.shots_left} shots")
            if self.last_shot: 
                prev_x, prev_y = self.last_shot
                prev_x =  string.ascii_uppercase[prev_x]
                print(">> Your last shot was: ", prev_x, prev_y + 1)
            
            try: 
                coordinates = input("Type the coordinates of your shot in the following format:\nLetterNumber, e.g. L0.\n")
                x = self.input_letter_to_num[coordinates[0].upper()]
                y = int(coordinates[1:]) - 1
                if not (0 <= y < self.solution.dim): raise ValueError
            except (ValueError, IndexError, KeyError): 
                print("Input not valid"); continue
            except KeyboardInterrupt: break

            self.shot((x, y))

        print("**** GAME OVER! ****")
        if no_ships_left : print("°°°°  You won! °°°°")
        else: print("You lost!")
        self.print_board(self.mask_reveal)



    def print_board(self, mask = None):
        if mask is None: mask = self.mask

        display = self.solution.board * mask
        # self.solution.board[mask]


        print(' ', *self.style["numbers"], sep = self.style["sep"])
        for i,letter in enumerate(self.style["letters"]):            
            print(letter, *(self.style["tiles"][tile] for tile in display[i]), letter, sep = self.style["sep"])
        print(' ', *self.style["numbers"], sep = self.style["sep"])   

class Board:
    def __init__(self, dim):  # building the empty board
        self.dim = dim
        
        self.board : np.array
        self.current_ship_id : int
        self.ships_coordinates : list
        self.ships_dimensions : list
        self.sunk_ships : list
        
        self.generate_board() # randomly generate game board 

    def generate_board(self):
        self.ships_dimensions = [4,3,3,2,2,2,1,1,1,1]
        self.ships_coordinates = []
        self.sunk_ships = [False for _ in self.ships_dimensions]

        while True:
            # reset values
            self.board = np.zeros((self.dim,self.dim), dtype = np.uint8)
            self.current_ship_id = FIRST_SHIP
            self.ships_coordinates.clear()

            # try to place all ships randomly
            for length in self.ships_dimensions:
                if not self.place_ship(length): break
                self.current_ship_id += 1
            else: # if the for loop exits by exhausting the iterable, exits the while loop. if it exits by breaking, the while loop is done once more
                # self.board[self.board == 0] = 1
                return

    def place_ship(self, length):        
        def boundary(direction): return length if direction else 1              # the initial coordinate can be anywhere on the board for this coordinate
                                                                                # the initial has to be on a reduced board to be able to continue the ship
        for _ in range(TRY_N_TIMES):                                            # ship generation can fail at most 10 times, before it returns False (= unsuccessful)
            dx = random.randint(0,1); dy = 1 - dx                               # ship direction is random

            x_i = random.randint(0, self.dim - boundary(dx)) # if ship is vertical x in [1,dim], y in [1,dim+1-ship.dim]; 
            y_i = random.randint(0, self.dim - boundary(dy)) # if ship is horizontal x in [1,dim+1-ship.dim], y in [1,dim]

            x_f = x_i + (length - 1) * dx                                         # ship's final position, calculated using direction and length
            y_f = y_i + (length - 1) * dy

            if self.board[x_i:x_f+1, y_i:y_f+1].any() : continue                # if there is a 1 or 2 on the board, try again
   
            fill_submatrix(self.board, x_i, x_f, y_i, y_f, WATER)
            self.board[x_i : x_f + 1, y_i : y_f + 1] = self.current_ship_id

            self.ships_coordinates.append((x_i, x_f, y_i, y_f))

            return True
        return False

    def reduce_ship_HP(self, ship_id):
        ship_id -= FIRST_SHIP
        self.ships_dimensions[ship_id] -= 1
        if self.ships_dimensions[ship_id]: # ship survived
            return False
        
        self.sunk_ships[ship_id] = True     # ship got sunk
        return True


game = Game(dim = 10, style = "emoji")
game.display_intro()
game.gameplay()


# dy = 1 - dx 
# dy = int(not dx)