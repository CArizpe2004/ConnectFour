class Game:
    def __init__(self):
        self.board = []
        self.turn = 'Player 1'
        self.icon = 'X'
        for i in range(9):
            row = [' '] * 7
            self.board.append(row)

        number_row = []
        for i in range(1, 8):
            number_row.append(str(i))
        self.board.append(number_row)
    def print_grid(self):
        for row in self.board:
            for col in row:
                print(col + ' | ', end='')
            print('\n' + '-' * 28)

    def get_col(self, row):
        row -= 1 
        i = 0
        if self.board[i][row] == ' ':
            while True:
                if i < 8:
                    if self.board[i + 1][row] == ' ':
                        i += 1
                    else:
                        return i
                else:
                    return i
        else:
            return i

    def change_turn(self):
        if self.turn == 'Player 1':
            self.turn = 'Player 2'
            self.icon = 'O'
        else:
            self.turn = 'Player 1'    
            self.icon = 'X'

    def check_for_winner(self):
        for row in reversed(range(9)):    
            for col in reversed(range(7)):
                itr = 0
                row_pointer = row
                col_pointer = col
                if row_pointer - 1 > 0:
                    if self.board[row_pointer][col] == self.icon:
                        itr += 1
                        while True:
                            row_pointer -= 1
                            if itr == 4:
                                return True
                            if row_pointer < 0:
                                break
                            if self.board[row_pointer][col] == self.icon:
                                itr += 1
                            else:
                                break
                if col + 1 < 8:
                    itr = 0
                    if self.board[row][col] == self.icon:
                        itr += 1
                        while True:
                            col_pointer += 1
                            if itr == 4:
                                return True
                            if col_pointer > 5:
                                break
                            if self.board[row][col_pointer] == self.icon:
                                itr += 1
                            else:
                                break
                if col - 1 >= 0 and row - 1 >= 0 and row + 1 < 9 and col + 1 < 7:
                    if self.board[row][col] == self.icon:
                        col_pointer = col - 1
                        row_pointer = row - 1
                        itr = 1
                        if self.board[row_pointer][col_pointer] == self.icon and self.board[row + 1][col + 1] == self.icon:
                            itr += 2
                            if row_pointer - 1 >= 0 and col_pointer - 1 >= 0:
                                if self.board[row_pointer - 1][col_pointer - 1] == self.icon:
                                    itr += 1
                            if row + 2 < 9 and col + 2 < 7:
                                if self.board[row + 2][col + 2] == self.icon:
                                    itr += 1
                            if itr >= 4:
                                return True
                        col_pointer = col - 1
                        row_pointer = row + 1
                        itr = 1
                        if self.board[row_pointer][col_pointer] == self.icon and self.board[row - 1][col + 1] == self.icon:
                            itr += 2
                            if row_pointer + 1 < 9 and col_pointer - 1 >= 0:
                                if self.board[row_pointer + 1][col_pointer - 1] == self.icon:
                                    itr += 1
                            if row - 2 >= 0 and col + 2 < 7:
                                if self.board[row - 2][col + 2] == self.icon:
                                    itr += 1
                            if itr >= 4:
                                return True
        return False
    
game = Game()
game.print_grid()

while True:
    num = input('Enter a Row ' + game.turn + ': > ')
    row = int(num)
    i = game.get_col(row)
    if i != 0:
        game.board[i][row - 1] = game.icon
    elif i == 0:
        if game.board[i][row - 1] == ' ':
            game.board[i][row - 1] = game.icon
    game.print_grid()
    if game.check_for_winner() == True:
        break
    game.change_turn()
print(game.turn + ' Wins!')