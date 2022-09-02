import numpy as np
import string
import random

TRY_N_TIMES = 10

class Game:
    def __init__(self, dim):
        self.shots_left = 50   # shots to end the game
        self.single_player = True
        self.board = Board(dim, 'traditional')

    def intro(self):
        if self.single_player: self.board.generate_board()       # randomly generate game board 
        # print("**** Welcome to the battleship game! ****")
        # print("The game board is 10x10 with rows ranging from 0 to 9 and columns from A to J\nIt is currently not possible to change the dimension of the board, but please stay tuned for updates.")
        # print("Press 'Ctrl+C' to exit at any time.")
        # print("****************************************")        
        # self.board.print_board()
        # print("****************************************")
        self.board.print_board()

class Board:
    def __init__(self, dim, board_style):  # building the empty board
        self.dim = dim
        # self.style = style(board_style)
        self.set_style(board_style)
        self.board = np.full((dim,dim), 0)
        self.ships_dimensions = [4,3,3,2,2,2,1,1,1,1]



    def set_style(self, new_style):
        # alternative emojis '⚪''🐱''🐶'   
        if new_style == 'emoji':
            self.style = {
                "tiles" : ['⚫', '🔵', '🚢', '❌'],
                "numbers" : ['1️⃣ ','2️⃣ ','3️⃣ ','4️⃣ ','5️⃣ ','6️⃣ ','7️⃣ ','8️⃣ ','9️⃣ ','🔟 '],
                "letters" : [ '🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯'], #🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙
                "sep" : '  '
                }

        elif new_style == 'traditional':
            self.style = {
                "tiles" : ['.', '~', '0', 'x'],
                "numbers" : [i for i in range(1, self.dim+1)],
                "letters" : string.ascii_uppercase[: self.dim],
                "sep" : ' '
                }


    def print_board(self):
        print(' ', *self.style["numbers"], sep = self.style["sep"])
        for i,letter in enumerate(self.style["letters"]):            
            # print(letter, end = self.style["sep"])
            # for j in range(self.dim):
            #     tile = self.board[i,j]
            #     print(self.style["tiles"][tile], end = self.style["sep"])
            # print()

            print(letter, *(self.style["tiles"][tile] for tile in self.board[i]), sep = self.style["sep"])
            # print(letter, *map(lambda tile: self.style["tiles"][tile], self.board[i]), sep = self.style["sep"])


    def generate_board(self):
        # ship = Ship(self, 2)
        # ship.gen_elements()
        while True:
            self.board = np.full((self.dim,self.dim), 0)
            ships_dim = [4,3,3,2,2,2,1,1,1,1] #[4,3]
            success = 0
            #for dim in self.ships_dimensions:
            for dim in ships_dim:
                ship = Ship(self, dim)
                if ship.gen_elements(): success += 1
            if success == len(ships_dim): break    

class Ship:
    def __init__(self, board, dim):
        self.dim = dim
        self.coords = []
        self.surround = []
        self.board = board

    def gen_elements(self):        
        global TRY_N_TIMES
        for _ in range(TRY_N_TIMES):                                            # ship generation can fail at most 10 times, before it returns False (= unsuccessful)
            dx, dy = random.choice([(0, 1), (1, 0)])                            # ship direction is random

            r_full_board = random.randint(0, self.board.dim-1)                  # the initial coordinate can be anywhere on the board for this coordinate
            r_reduced_board = random.randint(0, self.board.dim-self.dim)        # the initial has to be on a reduced board to be able to continue the ship

            x_i = r_full_board if dy else r_reduced_board                       # if ship is vertical x in [1,dim], y in [1,dim+1-ship.dim]; 
            y_i = r_full_board if dx else r_reduced_board                       # if ship is horizontal x in [1,dim+1-ship.dim], y in [1,dim]

            x_f = x_i + (self.dim-1)*dx                                             # ship's final position, calculated using direction and length
            y_f = y_i + (self.dim-1)*dy

            #x_i, x_f, y_i, y_f = (0,3,0,0)
            #print(x_i, x_f, y_i, y_f)
            if self.board.board[x_i:x_f+1, y_i:y_f+1].any() : continue          # if there is a 1 or 2 on the board, try again
            
            sx = max(0, x_i-1)                                                  # to deal with the lower border of the board
            sy = max(0, y_i-1)

            self.board.board[sx:x_f+2, sy:y_f+2] = 1                            # surroundings of the ship must be water
            self.board.board[x_i:x_f+1, y_i:y_f+1] = 2                          # now place the ship
            
            return True
        print("nope")
        return False

game = Game(10)
game.board.generate_board()
game.board.print_board()