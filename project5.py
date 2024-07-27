import pygame
from columns_rules import ColumnsGame, Jewel
import random

rows = 13
cols = 6
board = ColumnsGame(rows, cols, "EMPTY")

frozen = pygame.Color(0, 0, 0)
empty = pygame.Color(255, 0, 0)

S = 'S'
T = 'T'  
V = 'V'  
W = 'W' 
X = 'X'  
Y = 'Y'  
Z = 'Z'   

colors = [S, T, V, W, X, Y, Z]

class ColumnsGame2:
    '''
    Main class for the game
    '''
    def __init__(self):
        '''
        Initializes the game
        '''
        self.going = True
        self.game_board = board.getboard()
        self.look = False
        self.count = 0

    def jewel(self) -> list:
        '''
        Generates a random falling piece
        '''
        # Randomly select three jewel types for a falling piece
        first = random.choice(colors)
        second = random.choice(colors)
        third = random.choice(colors)
        return [first, second, third]

    def draw_board(self):
        '''
        Draw the game board on the display
        '''
        surface = pygame.display.get_surface()
        w, h = pygame.display.get_surface().get_size()
        y = 0
        # Draw rectangles for each cell on the game board
        for row in range(rows):
            y += 40
            x = 0
            for col in range(cols):
                x += 40
                rect = pygame.Rect((x * w) / 600, (y * h) / 600, (40 * w) / 600, (40 * h) / 600)
                pygame.draw.rect(surface, empty, rect, 1)

    def gamestate(self) -> None:
        '''
        Update the display with the current state of the game board
        '''
        surface = pygame.display.get_surface()
        w, h = pygame.display.get_surface().get_size()
        y = 0
        self.count = 0
        # Iterate through each cell on the game board
        for row in range(rows):
            y += 40
            x = 0
            for col in range(cols):
                x += 40
                try:
                    # Check if the cell is not empty
                    if self.game_board[row][col] != '   ':
                        rect = pygame.Rect((x * w) / 600, (y * h) / 600, (40 * w) / 600, (40 * h) / 600)
                        # Draw rectangles with different colors based on jewel type
                        if 'S' in self.game_board[row][col]:
                            pygame.draw.rect(surface, (255, 69, 0), rect, 0) 

                        elif 'T' in self.game_board[row][col]:
                            pygame.draw.rect(surface, (34, 139, 34), rect, 0)  

                        elif 'V' in self.game_board[row][col]:
                            pygame.draw.rect(surface, (50, 205, 50), rect, 0)  

                        elif 'W' in self.game_board[row][col]:
                            pygame.draw.rect(surface, (255, 215, 0), rect, 0)  

                        elif 'X' in self.game_board[row][col]:
                            pygame.draw.rect(surface, (186, 85, 211), rect, 0)  

                        elif 'Y' in self.game_board[row][col]:
                            pygame.draw.rect(surface, (70, 130, 180), rect, 0) 

                        elif 'Z' in self.game_board[row][col]:
                            pygame.draw.rect(surface, (128, 0, 128), rect, 0)  

                        # Check conditions and update counters
                        if self.game_board[row][col].startswith('[') or self.game_board[row][col].startswith('|'):
                            self.count = 1
                            self.look = False
                        # Draw frozen cells with a different color
                        if self.game_board[row][col].startswith(' ') and self.count == 0:
                            self.look = True
                            self.count += 1
                            if self.count > 10:
                                self.count = 0
                                self.look = False 
                        # Draw frozen cells with a different color
                    if self.game_board[row][col].startswith(' ') and self.game_board[row][col] != '   ':
                        rect = pygame.Rect((x * w) / 600, (y * h) / 600, (40 * w) / 600, (40 * h) / 600)
                        pygame.draw.rect(surface, frozen, rect, 0)
                except IndexError:
                    pass

    def handle_events(self, jewel) -> None:
        '''
        Handle the game events
        '''
        # Iterate through events and handle specific key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.move_left(jewel)
                elif event.key == pygame.K_RIGHT:
                    board.move_right(jewel)
                elif event.key == pygame.K_SPACE:
                    jewel.rotatejewel()
                else:
                    pass


    def draw_again(self) -> None:
        '''
        Redraw the game display
        '''
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(200, 200, 200)) 
        self.draw_board()
        self.gamestate()
        pygame.display.flip()

    def _end_game(self) -> None:
        '''
        End the game
        '''
        self.going = False

    def _resize_surface(self, size: tuple[int, int]) -> None:
        '''
        Resize the game surface
        '''
        pygame.display.set_mode(size, pygame.RESIZABLE)

    def run(self) -> None:
        '''
        Main function to run the game
        '''
        pygame.init()

        # Set the initial size of the game surface
        self._resize_surface((600, 600))

        f = self.jewel()
        jewel = Jewel(random.randint(1, 6), f[0], f[1], f[2])
        board.drop_first(jewel)

        clock = pygame.time.Clock()
        time_counter = 0
        # Main game loop
        while self.going:
            clock.tick(30)
            # Check if a new falling piece needs to be generated
            if self.look:
                f = self.jewel()
                list1 = [1, 2, 3, 4, 5, 6]
                rand = random.choice(list1)
                # Check for game over condition based on the occupied cells in the top rows
                for row in range(rows):
                    for col in range(cols):
                        if self.game_board[row][col] != '   ' and row < 2:
                            try:
                                list1.remove(col + 1)
                            except ValueError:
                                print('GAME OVER')
                # Generate a random column for the new falling piece
                if rand not in list1:
                    try:
                        rand = random.choice(list1)
                    except IndexError:
                        list1 = [1, 2, 3, 4, 5, 6]
                        rand = random.choice(list1)

                # Create a new Jewel object and drop it onto the game board
                jewel = Jewel(rand, f[0], f[1], f[2])
                board.drop_first(jewel)
                self.look = False
            # Handle user input events
            self.handle_events(jewel)
            self.draw_again()
            # Update the falling and freezing of the current piece
            time_counter += 1
            if time_counter > 5:
                board.falling(jewel)
                board.freeze(jewel)
                time_counter = 0

        # Quit the pygame module when the game ends
        pygame.quit()

if __name__ == '__main__':
    ColumnsGame2().run() 

