
class Game:
    def __init__(self, row: int, column: int, start: str):
        self.public_row = row
        self.public_column = column
        self._start = start
        self.public_board = self.print_board()
        self.public_count = 0
        self.going = False
        self.c = 0
        self.second = False
        self.match = False
 
    def getboard(self):
        return self.public_board 

    def print_board(self):
        if self._start == 'EMPTY':
            # Generate an empty game board
            board = [['   ' for _ in range(self.public_column)] for _ in range(self.public_row)]
            return board
        elif self._start == 'CONTENTS':
            # Generate a game board with provided jewel contents
            board = []
            jewels = [input() for _ in range(self.public_row)]

            for jewel in jewels:
                temp = [' ' + char + ' ' for char in jewel]
                board.append(temp)

            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        # Shift jewels down the board
                        if board[x + 1][y] == '   ':
                            board[x + 1][y], board[x][y] = board[x][y], '   '
                    except IndexError:
                        pass

            return board
        else:
            exit()

    def left(self, fall):
        fall.col = int(fall.col)
        try:
        # Check if it's possible to move the falling piece to the left, if so then move it
            if fall.col != 1 and self.public_board[fall.public_f_count][int(fall.col) - 2] == '   ':
            # Move the falling piece to the left in each row
                for offset in range(3):
                    if fall.public_f_count - offset >= 0:
                        self.public_board[fall.public_f_count - offset][int(fall.col) - 2] = f'[{fall.public_faller[offset]}]'
                        self.public_board[fall.public_f_count - offset][int(fall.col) - 1] = '   '

            # Update the falling piece's column position
                if fall.public_f_count > 0:
                    fall.col -= 1
        except IndexError:
            pass
        finally:
            fall.col = str(fall.col)

    def right(self, fall):
        fall.col = int(fall.col)
        try:
            # Check if it's possible to move the falling piece to the right
            if fall.col < self.public_column and self.public_board[fall.public_f_count][int(fall.col)] == '   ':
            # Move the falling piece to the right in each row
                for offset in range(3):
                    if fall.public_f_count - offset >= 0:
                        self.public_board[fall.public_f_count - offset][int(fall.col)] = f'[{fall.public_faller[offset]}]'
                        self.public_board[fall.public_f_count - offset][int(fall.col) - 1] = '   '

            # Update the falling piece's column position
                if fall.public_f_count > 0:
                    fall.col += 1
        except IndexError:
        # Handle the case when moving to the right goes beyond the board boundary
            fall.col -= 1
        finally:
            fall.col = str(fall.col)

    def fall(self, fall):# drop first
        if not self.going:
            self.public_board[0][int(fall.col) - 1] = f'[{fall.public_faller[2]}]'
            self.going = True
            self.second = False
            fall.public_f_count = 0
            self.c = 0

    def falling(self, fall):
        x = self.public_row - 1
        if fall.public_f_count < self.public_row and \
                self.going and \
                self.public_board[fall.public_f_count - x][int(fall.col) - 1] == '   ':
            fall.public_f_count += 1
            fall.public_bottom_count += 1
            try:
                if fall.public_f_count > 0:
                    self.public_board[fall.public_f_count][int(fall.col) - 1] = f'[{fall.public_faller[2]}]'
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 1] = f'[{fall.public_faller[1]}]'
                if fall.public_f_count > 1:
                    self.public_board[fall.public_f_count - 2][int(fall.col) - 1] = f'[{fall.public_faller[0]}]'
                if fall.public_f_count > 2:
                    self.public_board[fall.public_f_count - 3][int(fall.col) - 1] = '   '
                fall.public_frozen = False
            except IndexError:
                pass
        placeholer = self.public_row - 1
        if fall.public_bottom_count == placeholer:
            self.land(fall)
        elif self.public_board[fall.public_f_count - x][int(fall.col) - 1] != '   ' and not fall.public_frozen:
            self.land(fall)
            self.second = True

    def land(self, fall):
        if fall.public_f_count == 0:
            self.public_board[fall.public_bottom_count][int(fall.col) - 1] = '|' + fall.public_faller[2] + '|'
        if fall.public_f_count > 0:
            self.public_board[fall.public_bottom_count][int(fall.col) - 1] = '|' + fall.public_faller[2] + '|'
            self.public_board[fall.public_bottom_count - 1][int(fall.col) - 1] = '|' + fall.public_faller[1] + '|'
        if fall.public_f_count > 1:
            self.public_board[fall.public_bottom_count - 2][int(fall.col) - 1] = '|' + fall.public_faller[0] + '|'
        self.public_count = 0
        fall.public_frozen = True

    def gameover(self, fall):
        if (fall.public_f_count == 0 or fall.public_f_count == 1) and fall.public_frozen and self.public_count == 0:
            print('Game Over')
            quit()
        else:
            pass

    def freeze(self, fall):
        try:
            if fall.public_frozen and self.going:
                if self.public_count == 1:
                    if fall.public_f_count == 0:
                        self.public_board[fall.public_bottom_count][int(fall.col) - 1] = ' ' + fall.public_faller[2] + ' '
                        self.gameover(fall)
                    if fall.public_f_count == 1:
                        self.public_board[fall.public_bottom_count][int(fall.col) - 1] = ' ' + fall.public_faller[2] + ' '
                        self.public_board[fall.public_bottom_count - 1][int(fall.col) - 1] = ' ' + fall.public_faller[
                            1] + ' '
                        self.gameover(fall)
                    if fall.public_f_count > 1:
                        if not self.second:
                            self.public_board[fall.public_bottom_count - 1][int(fall.col) - 1] = ' ' + fall.public_faller[
                                2] + ' '
                            self.public_board[fall.public_bottom_count - 2][int(fall.col) - 1] = ' ' + fall.public_faller[
                                1] + ' '
                            self.public_board[fall.public_bottom_count - 3][int(fall.col) - 1] = ' ' + fall.public_faller[
                                0] + ' '
                        else:
                            self.public_board[fall.public_bottom_count][int(fall.col) - 1] = ' ' + fall.public_faller[
                                2] + ' '
                            self.public_board[fall.public_bottom_count - 1][int(fall.col) - 1] = ' ' + fall.public_faller[
                                1] + ' '
                            self.public_board[fall.public_bottom_count - 2][int(fall.col) - 1] = ' ' + fall.public_faller[
                                0] + ' '
                    fall.public_bottom_count = 0
                    self.going = False
                    self.public_count = 0
                else:
                    self.public_count += 1
        except IndexError:
            pass

class Faller:
    def __init__(self, col, one, two, three):
        self.public_frozen = False
        self.col = col
        self.public_f_count = 0
        self.public_bottom_count = 0
        self._one = one
        self._two = two
        self._three = three
        self.public_faller = [one, two, three]

    def rotateFaller(self):
        self.public_faller = self.public_faller[-1:] + self.public_faller[-3:-1]

import pygame
import friend as l
import random

rows = 13
cols = 6
board = l.Game(rows, cols, "EMPTY")

frozen = pygame.Color(0, 0, 0)
empty = pygame.Color(255, 255, 255)

S = 'S'  # pygame.Color(255,0,0)
T = 'T'  # pygame.Color(255,0,0)
V = 'V'  # pygame.Color(255,0,0)
W = 'W'  # pygame.Color(255,0,0)
X = 'X'  # pygame.Color(255,0,0)
Y = 'Y'  # pygame.Color(255,0,0)
Z = 'Z'  # pygame.Color(255,0,0) 

colors = [S, T, V, W, X, Y, Z]

class Project5:
    def __init__(self):
        self._running = True
        self.public_board = board.getboard()
        self.check = False
        self.count = 0
        self.full = []

    def faller(self) -> list:
        one = random.choice(colors)
        two = random.choice(colors)
        three = random.choice(colors)
        return [one, two, three]

    def draw_board(self):
        surface = pygame.display.get_surface()
        w, h = pygame.display.get_surface().get_size()
        y = 0
        for row in range(rows):
            y += 40
            x = 0
            for col in range(cols):
                x += 40
                rect = pygame.Rect((x * w) / 600, (y * h) / 600, (40 * w) / 600, (40 * h) / 600)
                pygame.draw.rect(surface, empty, rect, 1)

    def updateboard(self) -> None:
        surface = pygame.display.get_surface()
        w, h = pygame.display.get_surface().get_size()
        y = 0
        self.count = 0
        for row in range(rows):
            y += 40
            x = 0
            for col in range(cols):
                x += 40
                try:
                    if self.public_board[row][col] != '   ':
                        rect = pygame.Rect((x * w) / 600, (y * h) / 600, (40 * w) / 600, (40 * h) / 600)
                        if 'S' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (255, 69, 0), rect, 0)  # Orange-Red

                        elif 'T' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (34, 139, 34), rect, 0)  # Forest Green

                        elif 'V' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (50, 205, 50), rect, 0)  # Lime Green

                        elif 'W' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (255, 215, 0), rect, 0)  # Gold

                        elif 'X' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (186, 85, 211), rect, 0)  # Medium Orchid

                        elif 'Y' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (70, 130, 180), rect, 0)  # Steel Blue

                        elif 'Z' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (128, 0, 128), rect, 0)  # Purple

                        if self.public_board[row][col].startswith('[') or self.public_board[row][col].startswith('|'):
                            self.count = 1
                            self.check = False
                            #print(self.public_board[row][col])
                        if self.public_board[row][col].startswith(' ') and self.count == 0:
                            #self.count = 1
                            #print(self.public_board[row][col])
                            self.check = True
                            self.count += 1
                            if self.count > 10:
                                self.count = 0
                                self.check = False 
                        #print(self.public_board[row][col])
                    if self.public_board[row][col].startswith(' ') and self.public_board[row][col] != '   ':
                        rect = pygame.Rect((x * w) / 600, (y * h) / 600, (40 * w) / 600, (40 * h) / 600)
                        pygame.draw.rect(surface, frozen, rect, 0)
                except IndexError:
                    pass

    def run(self) -> None:
        pygame.init()

        self._resize_surface((600, 600))

        f = self.faller()
        faller = l.Faller(random.randint(1, 6), f[0], f[1], f[2]) # create function that takes in 3 jewels and places into list
        board.fall(faller) # function that drops the jewels

        clock = pygame.time.Clock()
        time_counter = 0
        while self._running:
            clock.tick(30)
            if self.check:
                f = self.faller()
                list1 = [1, 2, 3, 4, 5, 6]
                rand = random.choice(list1)
                for row in range(rows):
                    for col in range(cols):
                        if self.public_board[row][col] != '   ' and row < 2:
                            try:
                                list1.remove(col + 1)
                            except ValueError:
                                print('GAME OVER')
                if rand not in list1:
                    try:
                        rand = random.choice(list1)
                    except IndexError:
                        list1 = [1, 2, 3, 4, 5, 6]
                        rand = random.choice(list1)

                faller = l.Faller(rand, f[0], f[1], f[2]) # create function that takes in 3 jewels and places into list
                board.fall(faller) # function that drops the jewels
                self.check = False
            self._handle_events(faller)
            self._redraw()
            time_counter += 1
            if time_counter > 5:
                board.falling(faller) # 
                board.freeze(faller)
                time_counter = 0

        pygame.quit()

    def _handle_events(self, faller) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.left(faller)
                elif event.key == pygame.K_RIGHT:
                    board.right(faller)
                elif event.key == pygame.K_SPACE:
                    faller.rotateFaller()
                else:
                    pass

    def _redraw(self) -> None:
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(200, 200, 200)) # Orange
        self.draw_board()
        self.updateboard()
        pygame.display.flip()

    def _end_game(self) -> None:
        self._running = False

    def _resize_surface(self, size: tuple[int, int]) -> None:
        pygame.display.set_mode(size, pygame.RESIZABLE)


if __name__ == '__main__':
    Project5().run() 

