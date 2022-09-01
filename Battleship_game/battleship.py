import numpy as np
import string
import random

# alternative emojis '⚪''🐱''🐶'
def style(type):
        if type == 'emoji':
            return {'name': 'emoji','empty':'⚫', 'water': '🔵', 'ship': '🚢', 'sunk_ship': '❌'}
        else : 
            return {'name': 'traditional','empty':'.', 'water': '~', 'ship': '0', 'sunk_ship': 'x'}

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
        self.style = style(board_style)
        self.board = np.full((dim,dim), 0)
        self.ships_dimensions = [4,3,3,2,2,2,1,1,1,1]

    def set_style(self, new_style):
        if self.style['name'] == 'emoji':
            numbers = ['1️⃣ ','2️⃣ ','3️⃣ ','4️⃣ ','5️⃣ ','6️⃣ ','7️⃣ ','8️⃣ ','9️⃣ ','🔟 ']
            letters = [ '🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯'] #🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙
            sep = '  '     
        elif self.style['name'] == 'traditional':
            numbers = [i for i in range(1, self.dim+1)]
            letters = string.ascii_uppercase[: self.dim]
            sep = ' '


    def print_board(self):

    
        print(' ', *numbers, sep = sep)
        for i,letter in enumerate(letters):
            print(letter, *self.board[i], sep = sep)
        

    def generate_board(self):
        # ship = Ship(self, 2)
        # ship.gen_elements()
        global TRY_N_TIMES
        for i, dim in enumerate(self.ships_dimensions):
        # for i, dim in enumerate([4,3]):
            ship = Ship(self, dim)
            if not ship.gen_elements(): self.generate_board(); TRY_N_TIMES = 10
        print(self.board)


        # print(self.board)
        # while len(self.ships_dimensions):  # repeat until we have all the ships we want
        #     if not ship.gen_elements(): self.ships_dimensions = [4,3,3,2,2,2,1,1,1,1]; self.board.clear()
        #     else: 
        #     # self.board = np.full((self.dim,self.dim), self.style['empty'])
        #     self.ships_list.clear()                                # resets the list of ships, either at the beginning or in the case of unsuccessfult positioning


        #         for _ in range(TRY_N_TIMES):
        #             ship_placed = self.place_ship_random(dim)
        #             if ship_placed: break
        #         if not ship_placed: break



        #     if j>10: print(self.ships_list); print("AAAAAAAAAAAAAA"); exit(); break

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

            # x_i, x_f, y_i, y_f = (0,0,0,0)
            # print(x_i, x_f, y_i, y_f)
            if self.board.board[x_i:x_f+1, y_i:y_f+1].any() : continue          # if there is a 1 or 2 on the board, try again
            else:
                subs_1 = (x_f +2) if not x_i else (y_f +2)
                subs_2 = (x_f +2) if not x_i else (y_f +2)

                if not x_i and not y_i: self.board.board[:x_f+2, y_i:y_f+2] = 1
                elif not x_i:
                    self.board.board[:x_f+2, y_i-1:y_f+2] = 1
                elif not y_i:
                    self.board.board[x_i-1:x_f+2,:y_f+2, ] = 1
                    
                self.board.board[x_i-1:x_f+2, y_i-1:y_f+2] = 1
                self.board.board[x_i:x_f+1, y_i:y_f+1] = 2                      # 2 corresponds to a ship, 1 to the surroundings -> forbidden space
                
                return True
        return False

        # self.coords.append((x, y))        
        # for _ in range(1, self.dim):
        #     x += dx; y += dy

        #     self.coords.append((x,y))

game = Game(10)
#game.board.print_board()
game.board.generate_board()