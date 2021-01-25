class TicTacToe:
    def __init__(self):
        # uses a single list to represent 3 by 3 board
        self.board = [' ' for _ in range(9)]

        # keeps track of the winner
        self.current_winner = None

    def print_board(self):
        # prints the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # tells us what number corresponds to which box
        # 0 | 1 | 2 ...
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # # create list and assign tuples
        # # ['x', 'x', 'o'] --> [(0,'x'), (1,'x'), (2,'o')]
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

