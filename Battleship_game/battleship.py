import numpy as np
import string
import random

# style_types = ['emoji', 'traditional']
# alternative emojis '⚪''🐱''🐶'
def style(type):
        if type == 'emoji':
            return {'empty':'⚫', 'water': '🔵', 'ship': '🚢', 'sunk_ship': '❌'}
        else : 
            return {'empty':'.', 'water': '-', 'ship': '0', 'sunk_ship': 'x'}

TRY_N_TIMES = 10

class Game:
    def __init__(self, dim):
        self.shots_left = 50   # shots to end the game
        self.single_player = True
        self.board_dimension = dim
        self.solution = Board(dim, 'emoji')
        self.player_board = Board(dim, 'traditional')

    def intro(self):
        if self.single_player: self.solution.generate_board()       # randomly generate game board 
        # self.player_board.ships_list = self.solution.ships_list
        # print("**** Welcome to the battleship game! ****")
        # print("The game board is 10x10 with rows ranging from 0 to 9 and columns from A to J\nIt is currently not possible to change the dimension of the board, but please stay tuned for updates.")
        # print("Press 'Ctrl+C' to exit at any time.")
        # print("****************************************")        
        self.player_board.print_board()
        print("****************************************")
        self.solution.print_board()


class Board:
    def __init__(self, dim, board_style):  # building the empty board
        self.dim = dim
        self.style_type = board_style
        self.style = style(board_style)
        self.board = np.full((dim,dim), self.style['empty'])
        self.ships_dimensions = [4,3,3,2,2,2,1,1,1,1]
        self.ships_list = []
        

    def print_board(self):
        if self.style_type == 'emoji':
            numbers = ['1️⃣ ','2️⃣ ','3️⃣ ','4️⃣ ','5️⃣ ','6️⃣ ','7️⃣ ','8️⃣ ','9️⃣ ','🔟 ']
            letters = [ '🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯'] #🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙
            sep = '  '     
        elif self.style_type == 'traditional':
            numbers = [i for i in range(1, self.dim+2)]
            # letters = string.ascii_uppercase[:self.dim+1]
            letters = "ABCDEFGHIJ"
            sep = ' '
    
        print(' ', *numbers, sep = sep)
        for i,letter in enumerate(letters):
            print(letter, *self.board[i], sep = sep)


    def generate_board(self):
        j = 0
        while len(self.ships_list) != len(self.ships_dimensions):  # repeat until we have all the ships we want
            self.ships_list.clear()                                # resets the list of ships, either at the beginning or in the case of unsuccessfult positioning
            j += 1
            for dim in self.ships_dimensions:
                for _ in range(TRY_N_TIMES):
                    ship_placed = self.place_ship_random(dim)
                    if ship_placed: break
                
                if not ship_placed: break
            if j>10: print(self.ships_list); print("AAAAAAAAAAAAAA"); break
    
    # def place_ship_random(self, dim):
        
        # ship = Ship(dim)
        # ship.set_elements(self)

        # for ship_on_board in self.ships_list:
        #     ship_board = Ship(len(ship_on_board))
        #     ship_board.coords = ship_on_board
        #     ship_board.set_surr(self)
        #     for el in ship.coords:
        #         if el in ship_on_board or el in ship_board.surround: return False

        # self.ships_list.append(ship.coords)
        # for el in ship.coords:
        #     el_x, el_y = el
        #     self.board[el_x][el_y]= self.style['ship']
        # ship.set_surr(self)
        # for el in ship.surround:
        #     el_x, el_y = el
        #     self.board[el_x][el_y]= self.style['water']

        # return True

    def place_ship_random(self, dim):
        ship = Ship(self, dim)
        ship.gen_random_elements()
        for x,y in ship.coords:
            if self.board[x][y] in [self.style['ship'], self.style['water']]: 
                return False  # tried to generate ship on another ship or on its surrounding water
            self.board[x][y]= self.style['ship']

        self.ships_list.append(ship.coords)
        ship.gen_surr()
        for el in ship.surround:
            el_x, el_y = el
            self.board[el_x][el_y]= self.style['water']
        

        return True                

class Ship:
    def __init__(self, board, dim):
        self.dim = dim
        self.coords = []
        self.surround = []
        self.board = board

    def gen_random_elements(self):
        direction_switch = [(0, 1), (1, 0)]  # [right, down]
        # dx, dy = direction_switch[random.randint(0,1)]
        dx, dy = random.choice(direction_switch)

        r_full_board = random.randint(0, self.board.dim-1)
        r_reduced_board = random.randint(0, self.board.dim-self.dim)

        x = r_full_board if dy else r_reduced_board      #if down x in [1,10], y in [1,11-dim]; if right x in [1,11-dim], y in [1,10]
        y = r_full_board if dx else r_reduced_board

        self.coords.append((x, y))        
        for _ in range(1, self.dim):
            x += dx; y += dy
            self.coords.append((x,y))

    def gen_surr(self):
        # surr_points = [
        #     (-1,-1), (0,-1), (1,-1),
        #     (-1, 0),         (1, 0),
        #     (-1, 1), (0, 1), (1, 1)
        #     ]

        surr_points = [(1,0), (-1,0), (1,1),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1)]


        for el_x, el_y in self.coords:
            for dx, dy in surr_points:
                x = el_x + dx; y = el_y + dy
                if (0 <= x < self.board.dim) and (0 <= y < self.board.dim):
                    surr = (x, y)
                    if surr not in self.coords: 
                        self.surround.append(surr)


game = Game(10)
game.intro()