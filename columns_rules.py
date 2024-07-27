class Jewel:
    '''
    Class representing the falling piece in the game
    '''
    def __init__(self, col, first, second, third):
        self.frozen_piece = False
        self.col = col
        self.public_bottom_count = 0
        self._first = first
        self._second = second
        self._third = third
        self.current_jewel = [first, second, third]

    def rotatejewel(self):   
        '''
        Rotates faller
        '''
        self.current_jewel = self.current_jewel[-1:] + self.current_jewel[-3:-1]

class ColumnsGame:
    def __init__(self, row: int, column: int, begin: str):
        '''
        Class representing the game board and its operations
        '''
        self.game_row = row
        self.game_column = column
        self.begin = begin
        self.game_board = self.print_board()
        self.moving = False
        self.next = False

    def getboard(self):
        '''
        Get the current state of the game board
        '''
        return self.game_board 

    def print_board(self):
        '''
        Generate the initial game board
        '''
        if self.begin == 'EMPTY':
        # Generate an empty game board
            board = [['   ' for _ in range(self.game_column)] for _ in range(self.game_row)]
            return board
        elif self.begin == 'CONTENTS':
        # Generate a game board with provided jewel contents
            board = []
            jewels = [input() for _ in range(self.game_row)]

            for jewel in jewels:
                temp = [' ' + char + ' ' for char in jewel]
                board.append(temp)

            for y in range(self.game_row):
                for x in range(self.game_column):
                    try:
                        # Shift jewels down the board
                        if board[x + 1][y] == '   ':
                            board[x + 1][y], board[x][y] = board[x][y], '   '
                    except IndexError:
                        pass

            return board
        else:
            exit()

    def move_right(self, fall):
        '''
        Move the falling piece to the right on the game board
        '''
        fall.col = int(fall.col)
        try:
        # Check if it's possible to move the falling piece to the right
            if fall.col < self.game_column and self.game_board[fall.public_f_count][int(fall.col)] == '   ':
            # Move the falling piece to the right in each row
                for offset in range(3):
                    if fall.public_f_count - offset >= 0:
                        self.game_board[fall.public_f_count - offset][int(fall.col)] = f'[{fall.current_jewel[offset]}]'
                        self.game_board[fall.public_f_count - offset][int(fall.col) - 1] = '   '

            # Update the falling piece's column position
                if fall.public_f_count > 0:
                    fall.col += 1
        except IndexError:
        # Handle the case when moving to the right goes beyond the board boundary
            fall.col -= 1
        finally:
            fall.col = str(fall.col)

    def move_left(self, fall):
        '''
        Move the falling piece to the left on the game board
        '''
        fall.col = int(fall.col)
        try:
            # Check if it's possible to move the falling piece to the left
            if fall.col != 1 and self.game_board[fall.public_f_count][int(fall.col) - 2] == '   ':
            # Move the falling piece to the left in each row
                for offset in range(3):
                    if fall.public_f_count - offset >= 0:
                        self.game_board[fall.public_f_count - offset][int(fall.col) - 2] = f'[{fall.current_jewel[offset]}]'
                        self.game_board[fall.public_f_count - offset][int(fall.col) - 1] = '   '

            # Update the falling piece's column position
                if fall.public_f_count > 0:
                    fall.col -= 1
        except IndexError:
            pass
        finally:
            fall.col = str(fall.col)

    def drop_first(self, fall):
        '''
        Start the fall of the falling piece on the game board
        '''
        if not self.moving:
            self.game_board[0][int(fall.col) - 1] = f'[{fall.current_jewel[2]}]'
            self.moving = True
            self.next = False
            fall.public_f_count = 0
            self.c = 0

    def falling(self, fall):
        '''
        Move the falling piece down the game board
        '''
        x = self.game_row - 1

    # Check if the falling jewel can move down
        if fall.public_f_count < self.game_row and self.moving and self.game_board[fall.public_f_count - x][int(fall.col) - 1] == '   ':
            fall.public_f_count += 1
            fall.public_bottom_count += 1

            try:
            # Update the falling jewel's position on the board
                if fall.public_f_count > 0:
                    self.game_board[fall.public_f_count][int(fall.col) - 1] = f'[{fall.current_jewel[2]}]'
                    self.game_board[fall.public_f_count - 1][int(fall.col) - 1] = f'[{fall.current_jewel[1]}]'
                if fall.public_f_count > 1:
                    self.game_board[fall.public_f_count - 2][int(fall.col) - 1] = f'[{fall.current_jewel[0]}]'
                if fall.public_f_count > 2:
                    self.game_board[fall.public_f_count - 3][int(fall.col) - 1] = '   '

                fall.frozen_piece = False
            except IndexError:
                pass

        placeholder = self.game_row - 1

    # Check if the falling jewel has reached the bottom
        if fall.public_bottom_count == placeholder:
            self.land(fall)
    # Check if the falling jewel has landed on a frozen piece
        elif self.game_board[fall.public_f_count - x][int(fall.col) - 1] != '   ' and not fall.frozen_piece:
            self.land(fall)
            self.next = True

    def land(self, fall):
        '''
        Land the falling piece on the game board
        '''
        # If the falling piece is at the top row
        if fall.public_f_count == 0:
            self.game_board[fall.public_bottom_count][int(fall.col) - 1] = '|' + fall.current_jewel[2] + '|'
        # If the falling piece is at least one row down
        if fall.public_f_count > 0:
            self.game_board[fall.public_bottom_count][int(fall.col) - 1] = '|' + fall.current_jewel[2] + '|'
            self.game_board[fall.public_bottom_count - 1][int(fall.col) - 1] = '|' + fall.current_jewel[1] + '|'
        # If the falling piece is at least two rows down
        if fall.public_f_count > 1:
            # 
            self.game_board[fall.public_bottom_count - 2][int(fall.col) - 1] = '|' + fall.current_jewel[0] + '|'
        self.column_count = 0
        fall.frozen_piece = True


    def gameover(self, fall):
        '''
        End the game if the condition for the game over are met
        '''
        # Ends game if count is 0 and its frozen
        if (fall.public_f_count == 0 or fall.public_f_count == 1) and fall.frozen_piece and self.column_count == 0:
            print('Game Over')
            quit()
        else:
            pass

    def freeze(self, fall):
        '''
        Freeze the falling piece on the game board
        '''
        try:
            # Check if the falling piece is frozen and the game is in a moving state
            if fall.frozen_piece and self.moving:
                if self.column_count == 1:
                    if fall.public_f_count == 0:
                        self.game_board[fall.public_bottom_count][int(fall.col) - 1] = ' ' + fall.current_jewel[2] + ' '
                        self.gameover(fall)
                    if fall.public_f_count == 1:
                        # Update the game board with the frozen piece
                        self.game_board[fall.public_bottom_count][int(fall.col) - 1] = ' ' + fall.current_jewel[2] + ' '
                        self.game_board[fall.public_bottom_count - 1][int(fall.col) - 1] = ' ' + fall.current_jewel[
                            1] + ' '
                        self.gameover(fall)
                    if fall.public_f_count > 1:
                        if not self.next:
                            self.game_board[fall.public_bottom_count - 1][int(fall.col) - 1] = ' ' + fall.current_jewel[
                                2] + ' '
                            self.game_board[fall.public_bottom_count - 2][int(fall.col) - 1] = ' ' + fall.current_jewel[
                                1] + ' '
                            self.game_board[fall.public_bottom_count - 3][int(fall.col) - 1] = ' ' + fall.current_jewel[
                                0] + ' '
                        else:
                            self.game_board[fall.public_bottom_count][int(fall.col) - 1] = ' ' + fall.current_jewel[
                                2] + ' '
                            self.game_board[fall.public_bottom_count - 1][int(fall.col) - 1] = ' ' + fall.current_jewel[
                                1] + ' '
                            self.game_board[fall.public_bottom_count - 2][int(fall.col) - 1] = ' ' + fall.current_jewel[
                                0] + ' '
                    # Reset counters and flags
                    fall.public_bottom_count = 0
                    self.moving = False
                    self.column_count = 0
                else:
                    # Increment the column count
                    self.column_count += 1
        except IndexError:
            pass
