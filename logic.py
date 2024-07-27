class Game:
    def __init__(self, row: int, column: int, start: str):
        """just gets the variables ready you know for the program"""
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
        """Makes the game in a array, will look ugly, added this only to be able to do test driven development"""
        if self._start == 'EMPTY':
            """this one is for when EMPTY is entered"""
            field = []
            for col in range(self.public_row):
                field.append([])
                for row in range(self.public_column):
                    field[len(field) - 1].append('   ')
            return field
        elif self._start == 'CONTENTS':
            """this one is with contents, a 2d array """
            field = []
            jewel = []
            for col in range(self.public_row):
                jewel.append(input())
            for letter in jewel:
                temp = []
                for t in letter:
                    slot = ' ' + t + ' '
                    temp.append(slot)
                field.append(temp)
            for i in range(self.public_row):
                for y in range(self.public_row):
                    for x in range(self.public_column):
                        try:
                            if field[x + 1][y] == '   ':
                                field[x + 1][y] = field[x][y]
                                field[x][y] = '   '
                        except IndexError:
                            pass
            return field
        else:
            """I did not know what else to do please do not mark off points"""
            exit()

    def left(self, fall):
        """move left"""
        fall.col = int(fall.col)
        try:
            if fall.col != 1 and self.public_board[fall.public_f_count][int(fall.col) - 2] == '   ':
                if fall.public_f_count > -1:
                    self.public_board[fall.public_f_count][int(fall.col) - 2] = f'[{fall.public_faller[2]}]'
                    self.public_board[fall.public_f_count][int(fall.col) - 1] = '   '
                if fall.public_f_count > 0:
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 2] = f'[{fall.public_faller[1]}]'
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 1] = '   '
                if fall.public_f_count > 1:
                    self.public_board[fall.public_f_count - 2][int(fall.col) - 2] = f'[{fall.public_faller[0]}]'
                    self.public_board[fall.public_f_count - 2][int(fall.col) - 1] = '   '
                if fall.public_f_count > -1 or fall.public_f_count > 0 or fall.public_f_count > 1:
                    fall.col -= 1
        except IndexError:
            pass
        finally:
            fall.col = str(fall.col)

    def right(self, fall):
        """move right"""
        fall.col = int(fall.col)
        try:
            if fall.col < self.public_column and self.public_board[fall.public_f_count][int(fall.col)] == '   ':
                if fall.public_f_count > -1:
                    self.public_board[fall.public_f_count][int(fall.col)] = f'[{fall.public_faller[2]}]'
                    self.public_board[fall.public_f_count][int(fall.col) - 1] = '   '
                if fall.public_f_count > 0:
                    self.public_board[fall.public_f_count - 1][int(fall.col)] = f'[{fall.public_faller[1]}]'
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 1] = '   '
                if fall.public_f_count > 1:
                    self.public_board[fall.public_f_count - 2][int(fall.col)] = f'[{fall.public_faller[0]}]'
                    self.public_board[fall.public_f_count - 2][int(fall.col) - 1] = '   '
                if fall.public_f_count > -1 or fall.public_f_count > 0 or fall.public_f_count > 1:
                    fall.col += 1
        except IndexError:
            fall.col -= 1
        finally:
            fall.col = str(fall.col)

    def fall(self, fall):
        """Starts the fall for a faller, i.e. gets it started"""
        if not self.going:
            self.public_board[0][int(fall.col) - 1] = f'[{fall.public_faller[2]}]'
            self.going = True
            self.second = False
            fall.public_f_count = 0
            self.c = 0

    def isgoing(self):
        """returns if true if theres a faller falling"""
        if self.going:
            return True
        else:
            return False

    def falling(self, fall):
        """falls the faller through updating the board with a series of if statments"""
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
        """does the land thing so this: | |"""
        if fall.public_f_count == 0:
            self.public_board[fall.public_bottom_count][int(fall.col) - 1] = '|' + fall.public_faller[2] + '|'
        if fall.public_f_count > 0:
            self.public_board[fall.public_bottom_count][int(fall.col) - 1] = '|' + fall.public_faller[2] + '|'
            self.public_board[fall.public_bottom_count - 1][int(fall.col) - 1] = '|' + fall.public_faller[1] + '|'
        if fall.public_f_count > 1:
            self.public_board[fall.public_bottom_count - 2][int(fall.col) - 1] = '|' + fall.public_faller[0] + '|'
        self.public_count = 0
        fall.public_frozen = True

    def horizontal(self):
        """checks horizontal matching"""
        for i in range(self.public_row):
            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        # x = down
                        # y = right
                        if self.public_board[x][y] != '   ' and '*' not in self.public_board[x][y]:
                            if self.public_board[x][y] == self.public_board[x][y + 1] == self.public_board[x][y + 2]:
                                self.public_board[x][y] = '*' + self.public_board[x][y].strip() + '*'
                                self.public_board[x][y + 1] = '*' + self.public_board[x][y + 1].strip() + '*'
                                self.public_board[x][y + 2] = '*' + self.public_board[x][y + 2].strip() + '*'
                                self.match = True
                            if self.public_board[x][y] == self.public_board[x][y + 1] == self.public_board[x][y + 2] == self.public_board[x][y+3]:
                                self.public_board[x][y] = '*' + self.public_board[x][y].strip() + '*'
                                self.public_board[x][y + 1] = '*' + self.public_board[x][y + 1].strip() + '*'
                                self.public_board[x][y + 2] = '*' + self.public_board[x][y + 2].strip() + '*'
                                self.public_board[x][y + 2] = '*' + self.public_board[x][y + 3].strip() + '*'
                                self.match = True
                    except IndexError:
                        pass

    def dhorizontal(self):
        """makes the horizontal ones disapper"""
        for i in range(self.public_row):
            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        if self.public_board[x][y] != '   ' and '*' in self.public_board[x][y]:
                            if self.public_board[x][y] == self.public_board[x][y + 1] == self.public_board[x][y + 2]:
                                self.public_board[x][y] = '   '
                                self.public_board[x][y + 1] = '   '
                                self.public_board[x][y + 2] = '   '
                            if self.public_board[x][y] == self.public_board[x][y + 1] == self.public_board[x][y + 2] == self.public_board[x][y+3]:
                                self.public_board[x][y] = '   '
                                self.public_board[x][y + 1] = '   '
                                self.public_board[x][y + 2] = '   '
                                self.public_board[x][y + 3] = '   '
                    except IndexError:
                        pass

    def vertical(self):
        """match for vertical"""
        for i in range(self.public_row):
            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        if self.public_board[x][y] != '   ' and '*' not in self.public_board[x][y]:
                            if self.public_board[x][y] == self.public_board[x + 1][y] == self.public_board[x + 2][y]:
                                self.public_board[x][y] = '*' + self.public_board[x][y].strip() + '*'
                                self.public_board[x + 1][y] = '*' + self.public_board[x + 1][y].strip() + '*'
                                self.public_board[x + 2][y] = '*' + self.public_board[x + 2][y].strip() + '*'
                                self.match = True
                            if self.public_board[x][y] == self.public_board[x + 1][y] == self.public_board[x + 2][y] == self.public_board[x+3][y]:
                                self.public_board[x][y] = '*' + self.public_board[x][y].strip() + '*'
                                self.public_board[x + 1][y] = '*' + self.public_board[x + 1][y].strip() + '*'
                                self.public_board[x + 2][y] = '*' + self.public_board[x + 2][y].strip() + '*'
                                self.public_board[x + 3][y] = '*' + self.public_board[x + 2][y].strip() + '*'
                                self.match = True
                    except IndexError:
                        pass

    def dvertical(self):
        """removes vertical matches"""
        for i in range(self.public_row):
            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        if self.public_board[x][y] != '   ' and '*' in self.public_board[x][y]:
                            if self.public_board[x][y] == self.public_board[x + 1][y] == self.public_board[x + 2][y]:
                                self.public_board[x][y] = '   '
                                self.public_board[x + 1][y] = '   '
                                self.public_board[x + 2][y] = '   '
                            if self.public_board[x][y] == self.public_board[x + 1][y] == self.public_board[x + 2][y] == self.public_board[x+3][y]:
                                self.public_board[x][y] = '   '
                                self.public_board[x + 1][y] = '   '
                                self.public_board[x + 2][y] = '   '
                                self.public_board[x + 3][y] = '   '
                    except IndexError:
                        pass

    def diagonal(self):
        """checks for diagonal matches"""
        for i in range(self.public_row):
            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        if self.public_board[x][y] != '   ' and '*' not in self.public_board[x][y]:
                            if self.public_board[x][y] == self.public_board[x + 1][y - 1] == self.public_board[x + 2][y - 2]:
                                self.public_board[x][y] = '*' + self.public_board[x][y].strip() + '*'
                                self.public_board[x + 1][y - 1] = '*' + self.public_board[x + 1][y - 1].strip() + '*'
                                self.public_board[x + 2][y - 2] = '*' + self.public_board[x + 2][y -2].strip() + '*'
                                self.match = True
                            if self.public_board[x][y] == self.public_board[x + 1][y - 1] == self.public_board[x + 2][y - 2] == \
                                    self.public_board[x + 3][y - 3]:
                                self.public_board[x][y] = '*' + self.public_board[x][y].strip() + '*'
                                self.public_board[x + 1][y - 1] = '*' + self.public_board[x + 1][y - 1].strip() + '*'
                                self.public_board[x + 2][y - 2] = '*' + self.public_board[x + 2][y - 2].strip() + '*'
                                self.public_board[x + 3][y - 3] = '*' + self.public_board[x + 2][y - 3].strip() + '*'
                                self.match = True
                    except IndexError:
                        pass

    def ddiagonal(self):
        """removes matched diagonal"""
        for i in range(self.public_row):
            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        if self.public_board[x][y] != '   ' and '*' in self.public_board[x][y]:
                            if self.public_board[x][y] == self.public_board[x + 1][y - 1] == self.public_board[x + 2][y - 2]:
                                self.public_board[x][y] = '   '
                                self.public_board[x + 1][y-1] = '   '
                                self.public_board[x + 2][y-2] = '   '
                            if self.public_board[x][y] == self.public_board[x + 1][y - 1] == self.public_board[x + 2][
                                y - 2] == \
                                    self.public_board[x + 3][y - 3]:
                                self.public_board[x][y] = '   '
                                self.public_board[x + 1][y-1] = '   '
                                self.public_board[x + 2][y-2] = '   '
                                self.public_board[x + 3][y-3] = '   '
                    except IndexError:
                        pass


    def drop(self):
        """drops the jewels after the matched ones vanish"""
        for i in range(self.public_row):
            for y in range(self.public_row):
                for x in range(self.public_column):
                    try:
                        if self.public_board[x + 1][y] == '   ':
                            self.public_board[x + 1][y] = self.public_board[x][y]
                            self.public_board[x][y] = '   '
                    except IndexError:
                        pass

    def check_matching(self):
        """all the matching"""
        self.horizontal()
        self.vertical()
        self.diagonal()

    def disapper(self):
        """all the disappering and dropping it"""
        if self.match:
            self.dhorizontal()
            self.dvertical()
            self.ddiagonal()
            self.drop()
            self.match = False

    def gameover(self, fall):
        """checks itf it is game over"""
        if (fall.public_f_count == 0 or fall.public_f_count == 1) and fall.public_frozen and self.public_count == 0:
            print('Game Over')
            quit()
        else:
            pass

    def freeze(self, fall):
        """does the freeze so it makes it naked"""
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

    def notfalling(self, fall):
        """updates to rotate it for when it's not falling"""
        try:
            if not fall.public_frozen:
                if fall.public_f_count > 0:
                    self.public_board[fall.public_f_count][int(fall.col) - 1] = '[' + fall.public_faller[2] + ']'
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 1] = '[' + fall.public_faller[1] + ']'
                if fall.public_f_count > 1:
                    self.public_board[fall.public_f_count][int(fall.col) - 1] = '[' + fall.public_faller[2] + ']'
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 1] = '[' + fall.public_faller[1] + ']'
                    self.public_board[fall.public_f_count - 2][int(fall.col) - 1] = '[' + fall.public_faller[0] + ']'
                    self.public_board[fall.public_f_count - 3][int(fall.col) - 1] = '   '
                if fall.public_f_count > 2:
                    self.public_board[fall.public_f_count - 3][int(fall.col) - 1] = '   '
            else:
                if fall.public_f_count > 0:
                    self.public_board[fall.public_f_count][int(fall.col) - 1] = '|' + fall.public_faller[2] + '|'
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 1] = '|' + fall.public_faller[1] + '|'
                if fall.public_f_count > 1:
                    self.public_board[fall.public_f_count][int(fall.col) - 1] = '|' + fall.public_faller[2] + '|'
                    self.public_board[fall.public_f_count - 1][int(fall.col) - 1] = '|' + fall.public_faller[1] + '|'
                    self.public_board[fall.public_f_count - 2][int(fall.col) - 1] = '|' + fall.public_faller[0] + '|'
                    self.public_board[fall.public_f_count - 3][int(fall.col) - 1] = '   '
                if fall.public_f_count > 2:
                    self.public_board[fall.public_f_count - 3][int(fall.col) - 1] = '   '
        except ValueError:
            pass


def displayField(game):
    """prints the board according to the guide with the vertical bars and 3c dashes"""
    display = game.public_board
    for x in display:
        d = []
        for y in x:
            d.append(y)
        complete = ''.join(d)
        print('|' + complete + '|')
    c = '---' * game.public_column
    print(' ' + c + ' ')  # followed by another space


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
        """rotates it"""
        self.public_faller = self.public_faller[-1:] + self.public_faller[-3:-1]


import pygame
import logic as l
import random

rows = 13
cols = 6
board = l.Game(rows, cols, "EMPTY")

frozen = pygame.Color(0, 0, 0)
empty = pygame.Color(255, 255, 255)

A = 'A'  # pygame.Color(255,0,0)
B = 'B'  # pygame.Color(0,255,0)
C = 'C'  # pygame.Color(255,128,0)
D = 'D'  # pygame.Color(255,255,0)
E = 'E'  # pygame.Color(255,0,255)
F = 'F'  # pygame.Color(0,255,255)
G = 'G'  # pygame.Color(255,0,255)

colors = [A, B, C, D, E, F, G]


class Project5:
    def __init__(self):
        """variables for if it's going and more"""
        self._running = True
        self.public_board = board.getboard()
        self.check = False
        self.count = 0
        self.full = []

    def faller(self) -> list:
        """create the faller"""
        one = random.choice(colors)
        two = random.choice(colors)
        three = random.choice(colors)
        return [one, two, three]

    def draw_board(self):
        """draw board"""
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
        """update s ddfgbhuitrieutgjiketrsbnjkgbnledrtbjklegbvnil dtbnkl fngbkltvdtfbnk gjmk gjkedrb the baord"""
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
                        if 'A' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (255, 0, 0), rect, 0)
                        elif 'B' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (0, 255, 0), rect, 0)
                        elif 'C' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (255, 128, 0), rect, 0)
                        elif 'D' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (255, 255, 0), rect, 0)
                        elif 'E' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (255, 0, 255), rect, 0)
                        elif 'F' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (0, 255, 255), rect, 0)
                        elif 'G' in self.public_board[row][col]:
                            pygame.draw.rect(surface, (255, 0, 255), rect, 0)

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
        """main run function"""
        pygame.init()

        self._resize_surface((600, 600))

        f = self.faller()
        faller = l.Faller(random.randint(1, 6), f[0], f[1], f[2])
        board.fall(faller)

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

                faller = l.Faller(rand, f[0], f[1], f[2])
                board.fall(faller)
                self.check = False
            self._handle_events(faller)
            self._redraw()
            time_counter += 1
            if time_counter > 5:
                board.falling(faller)
                board.freeze(faller)
                time_counter = 0

        pygame.quit()

    def _handle_events(self, faller) -> None:
        """handles inputs"""
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
        """draws the board"""
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(100, 100, 100))
        self.draw_board()
        self.updateboard()
        pygame.display.flip()

    def _end_game(self) -> None:
        """ends the game"""
        self._running = False

    def _resize_surface(self, size: tuple[int, int]) -> None:
        """makes is resizable"""
        pygame.display.set_mode(size, pygame.RESIZABLE)


if __name__ == '__main__':
    """this thing"""
    Project5().run()
