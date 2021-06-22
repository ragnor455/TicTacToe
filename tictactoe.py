# TicTacToe
import random


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            self.turn = 'Player 1'
        else:
            self.turn = 'Player 2'

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                " board=" "|".join(self.board) +
                ">")

    def draw_board(self):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def input_player_letter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the first player's letter as the first item, and the second player's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the first player's letter, the second is the second player's letter.
        if letter == 'X':
            self.player_1_letter, self.player_2_letter = ['X', 'O']
        else:
            self.player_1_letter, self.player_2_letter = ['O', 'X']

    def play_again(self):
        # This function returns True if the players want to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def make_move(self):
        if self.turn == "Player 1":
            self.board[self.move] = self.player_1_letter
        else:
            self.board[self.move] = self.player_2_letter

    def is_space_free(self, board, move):
        # Return true if the passed move is free on the passed board.
        # Do not use self.board here because we also use the copied boards
        return board[move] == ' '

    def is_winner(self):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        bo = self.board
        if self.turn == 'player 1':
            le = self.player_1_letter
        else:
            le = self.player_2_letter
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or   # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or   # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or   # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or   # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or   # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or   # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or   # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))   # diagonal

    def get_board_copy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupe_board = []

        for i in self.board:
            dupe_board.append(i)

        return dupe_board

    def get_player_move(self):
        # Let the player type in their move.
        print('What is your next move? (1-9)')
        move = input()
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.is_space_free(self.board, int(move)):
            print('That was not a valid choice.')
            print('What is your next move? (1-9)')
            move = input()
        self.move = int(move)

    def choose_random_move_from_list(self, moves_list):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possible_moves = []
        for i in moves_list:
            if self.is_space_free(self.board, i):
                possible_moves.append(i)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None

    def is_board_full(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.is_space_free(self.board, i):
                return False
        return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board

    the_board = TicTacToe()
    the_board.input_player_letter()
    print(the_board.turn + ' will go first.')
    game_is_playing = True

    while game_is_playing:
        if the_board.turn == 'Player 1':
            # Player 1's turn.
            the_board.draw_board()
            the_board.get_player_move()
            the_board.make_move()

            if the_board.is_winner():
                the_board.draw_board()
                print('Player 1 has won the game! Player 2 loses.')
                gameIsPlaying = False
            else:
                if the_board.is_board_full():
                    the_board.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    the_board.turn = 'Player 2'

        else:
            # Player 2's turn.
            the_board.draw_board()
            the_board.get_player_move()
            the_board.make_move()

            if the_board.is_winner():
                the_board.draw_board()
                print('Player 2 has won the game! Player 1 loses.')
                gameIsPlaying = False
            else:
                if the_board.is_board_full():
                    the_board.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    the_board.turn = 'Player 1'

    if not the_board.play_again():
        break
