# creating a class for the entire game
class PyPacPoe():
    def __init__(self):
        self.current_player = 'X'
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
        print('''
                 A   B   C

            1)    |    | 
                -----------
            2)    |    |  
                -----------
            3)    |    |  
              ''')
    def display_turn(self):
        print(f'Player {self.current_player}\'s Move (example B2):')
    def get_move(self):
        move = input('Enter valid move: ').lower()
        #if not a1, b1 etc..valid move? if not in while checking object
        while not move in self.current_board:
            move = input('Invalid move, try again: ').lower()
        #if unavailable run loop again
        while self.current_board[move] != None:
            move = input('Already taken, try again: ').lower()
        self.current_board[move] = self.current_player
        return move 
    def display_win(self):
        # should be the last person who played
        print(f'{self.current_player} has won the game')
    def display_tie(self):
        print('It was a tie!')


new_game = PyPacPoe()
new_game.welcome_message()
new_game.display_board()
new_game.display_turn()
print(new_game.get_move())



