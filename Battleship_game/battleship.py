import numpy as np
import string
import random

TRY_N_TIMES = 10

class Game:
    def __init__(self, dim):
        self.shots_left = 50   # shots to end the game
        self.single_player = True
        self.solution = Board(dim, 'traditional')
        self.player_board = Board(dim, 'emoji')

    def intro(self):
        if self.single_player: self.solution.generate_board()       # randomly generate game board 
        #self.display.board = self.board.board.copy()
        # print("**** Welcome to the battleship game! ****")
        # print("The game board is 10x10 with rows ranging from 0 to 9 and columns from A to J\nIt is currently not possible to change the dimension of the board, but please stay tuned for updates.")
        # print("Press 'Ctrl+C' to exit at any time.")
        # print("****************************************")        
        # self.board.print_board()
        # print("****************************************")
        self.player_board.print_board()

    def shot (self, coordinates): 
        x, y = coordinates
        self.player_board.board[x][y] = max(1, self.solution.board[x][y])
        self.player_board.print_board()
        self.shots_left -= 1

    #     h = self.shots_left
    #     shot_type = ''
    #     for i, ship in enumerate(self.player_board.ships_list):
    #         for element in self.player_board.ships_list[i]:
    #             if len(ship) == 1 and coordinates == element : 
    #                 print("Hit and sunk!")
    #                 self.shots_left -= 1; self.player_board.ships_list.remove(ship)
    #                 shot_type = '#'; break
    #             if coordinates == element : 
    #                 print("Hit!") 
    #                 self.shots_left -= 1; ship.remove(element)
    #                 shot_type = 'o'; break
    #     if h == self.shots_left : 
    #         print("Miss!"); self.shots_left -= 1
    #         shot_type = 'x'
    #     print("Shots left: ", self.shots_left)
    #     return shot_type
    #     #board.update_board(board, coordinates)

    def gameplay(self):
        try:
            while self.shots_left:
                if not self.player_board.ships_dimensions : break
                print("You have a total of ", self.shots_left, " shots.")
                try: 
                    coordinates = input("Type the coordinates of your shot in the following format:\nLetterNumber, e.g. L0.\n")
                    x, y = coordinates
                except ValueError: print("Input not valid"); continue
                x = x.upper()
                if x not in "ABCDEFGHIJ": print("Input not valid"); continue    # hard coded, works only for a 10x10 board. Use string.asciiletters in the future           
                try: y = int(y)+1
                except: print("not valid"); continue
                if y < 1 or y > 9 : print("not valid"); continue
                for i, letter in enumerate("ABCDEFGHIJ"):   # string.ascii_uppercase): 
                    if x == letter: x = i+1

                self.shot((x, y))

        except KeyboardInterrupt: pass
        print("**** GAME OVER! ****")
        if not self.player_board.ships_list : print("°°°°  You won! °°°°")
        else: print("You lost!")
        print(self.solution.board)

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
            print(letter, *(self.style["tiles"][tile] for tile in self.board[i]), sep = self.style["sep"])
            # print(letter, *map(lambda tile: self.style["tiles"][tile], self.board[i]), sep = self.style["sep"])

    def place_ship(self, dim):        
        global TRY_N_TIMES
        for _ in range(TRY_N_TIMES):                                            # ship generation can fail at most 10 times, before it returns False (= unsuccessful)
            dx, dy = random.choice([(0, 1), (1, 0)])                            # ship direction is random

            r_full_board = random.randint(0, self.dim-1)                        # the initial coordinate can be anywhere on the board for this coordinate
            r_reduced_board = random.randint(0, self.dim-dim)                   # the initial has to be on a reduced board to be able to continue the ship

            x_i = r_full_board if dy else r_reduced_board                       # if ship is vertical x in [1,dim], y in [1,dim+1-ship.dim]; 
            y_i = r_full_board if dx else r_reduced_board                       # if ship is horizontal x in [1,dim+1-ship.dim], y in [1,dim]

            x_f = x_i + (dim-1)*dx                                              # ship's final position, calculated using direction and length
            y_f = y_i + (dim-1)*dy

            #x_i, x_f, y_i, y_f = (0,3,0,0)
            #print(x_i, x_f, y_i, y_f)
            if self.board[x_i:x_f+1, y_i:y_f+1].any() : continue                # if there is a 1 or 2 on the board, try again
            
            sx = max(0, x_i-1)                                                  # to deal with the lower border of the board
            sy = max(0, y_i-1)

            self.board[sx:x_f+2, sy:y_f+2] = 1                                  # surroundings of the ship must be water
            self.board[x_i:x_f+1, y_i:y_f+1] = 2                                # now place the ship
            
            return True
        return False

    def generate_board(self):
        # ship = Ship(self, 2)
        # ship.gen_elements()
        while True:
            self.board = np.full((self.dim,self.dim), 0)
            ships_dim = [4,3,3,2,2,2,1,1,1,1] #[4,3]
            success = 0
            #for dim in self.ships_dimensions:
            for dim in ships_dim:
                if self.place_ship(dim): success += 1
            if success == len(ships_dim): break    

class Ship:
    def __init__(self, coords, surr, dim):
        self.dim = dim
        self.coords = coords
        self.surround = surr
        self.hit_counter = 0

    

game = Game(10)
game.intro()
game.gameplay()