# creating a class for the entire game
class PyPacPoe():
    def __init__(self):
        self.current_player = 'X'
        self.num_turns = 0
        self.is_winner = False
        self.is_tie = False
        self.current_board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None
        }
    # see welcome message
    
    def welcome_message(self):
        print('''
        ---------------------
        Welcome to Py-Pac-Poe
        Let's Play!
        ---------------------
        ''')
    
    def display_board(self):
        print(f'''
                 A   B   C

            1)  {self.current_board['a1']} | {self.current_board['b1']} | {self.current_board['c1']} 
                ----------------
            2)  {self.current_board['a2']} | {self.current_board['b2']} | {self.current_board['c2']} 
                ----------------
            3)  {self.current_board['a3']} | {self.current_board['b3']} | {self.current_board['c3']}  
              ''')
    
    def display_turn(self):
        print(f'Player {self.current_player}\'s Move (example B2):')
    
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
    
    def get_move(self):
        move = input('Enter valid move: ').lower()
        #if not a1, b1 etc..valid move? if not in while checking object
        while not move in self.current_board:
            self.display_board()
            move = input('Invalid move, try again: ').lower()
        #if unavailable run loop again
        while self.current_board[move] != None:
            self.display_board()
            move = input('Already taken, try again: ').lower()
        self.current_board[move] = self.current_player
        self.num_turns += 1
        self.display_board()
    
    def check_win(self):
        if self.current_board['a1'] == self.current_player and self.current_board['b1'] == self.current_player and self.current_board['c1'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.current_board['a2'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['c2'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.current_board['a3'] == self.current_player and self.current_board['b3'] == self.current_player and self.current_board['c3'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.current_board['a1'] == self.current_player and self.current_board['a2'] == self.current_player and self.current_board['a3'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.current_board['b1'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['b3'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.current_board['c1'] == self.current_player and self.current_board['c2'] == self.current_player and self.current_board['c3'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.current_board['a1'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['c3'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.current_board['a3'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['c1'] == self.current_player:
            self.is_winner = True
            self.display_win()
        elif self.num_turns == 9 and not self.is_winner:
            self.is_tie = True
            self.display_tie()
        return
    
    def display_win(self):
        # should be the last person who played
        print(f'{self.current_player} has won the game')
    
    def display_tie(self):
        print('It was a tie!')
    
    def play_game(self):
        while not self.is_winner and not self.is_tie:
            self.display_board()
            self.display_turn()
            self.get_move()
            self.check_win()
            self.switch_player()
    def init_game(self):
        self.welcome_message()
        self.play_game()


new_game = PyPacPoe()
# new_game.welcome_message()
# new_game.display_turn()
# new_game.get_move()
# new_game.switch_player()
new_game.init_game()


