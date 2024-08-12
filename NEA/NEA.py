import pygame
import os
import sys

# Initiate modules
pygame.init()
pygame.font.init()

# Screen
resolution = width, height = 1920, 1080
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("King's Quest")

# FPS
clock = pygame.time.Clock()
fps = 60

# Colours
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (50, 175, 50)
MID_GREEN = (35, 220, 35)
RED = (255, 0, 0)
DARK_RED = (155, 70, 70)

PIECES = ["N", "Q", "B", "R", "K"]



class Load_Save():

    def __init__(self):
        pass
    
    @classmethod
    def save_level(self, board, filename):

        file = open(os.path.join("Levels", "User Levels", filename), "w")
        for i in range(len(board)):
            for j in range(len(board[i])):
                if j % 21 == 0 and j != 0:
                    file.write(board[i][j] + "\n")
                else:
                    file.write(board[i][j])
        file.close()

    @classmethod
    def load_level(self, filepath):

        board = list()
        file = open(filepath, 'r')
        for i in range(16):
            board.append(list(file.readline()))
            board[i].remove("\n")
        file.close()

        return board


class Player():

    def __init__(self, cell):

        self.cell = cell
        image = pygame.image.load(os.path.join("Assets", "Pieces", "white king.png"))
        self.image = pygame.transform.scale(image, (cell.cell_size, cell.cell_size))

        self.x = cell.x
        self.y = cell.y
    
    def draw_player(self):

        screen.blit(self.image, (self.cell.x, self.cell.y))

    @classmethod
    def moves(self, board, coord):
        '''
        Returns the set of all possible moves as a tuple (i, j)
        '''
        possible_moves = set()
        x, y = coord

        for j in range(len(board)):
            for i in range(len(board[j])):
                if (abs(x - i) == 1 and abs(y - j) == 1) or (abs(x - i) == 1 and abs(y - j) == 0) or (abs(x - i) == 0 and abs(y - j) == 1):
                    possible_moves.add((i, j))

        return possible_moves
     

class Knight():

    def __init__(self, cell):

        self.cell = cell
        image = pygame.image.load(os.path.join("Assets", "Pieces", "black knight.png"))
        self.image = pygame.transform.scale(image, (cell.cell_size, cell.cell_size))

        self.x = cell.x
        self.y = cell.y
    
    def draw_knight(self):

        screen.blit(self.image, (self.cell.x, self.cell.y))

    @classmethod
    def moves(self, board, coord):
        '''
        Returns the set of all possible moves as a tuple (i, j)
        '''
        possible_moves = set()
        x, y = coord

        for j in range(len(board)):
            for i in range(len(board[j])):
                if (abs(x - i) == 1 and abs(y - j) == 1) or (abs(x - i) == 1 and abs(y - j) == 0) or (abs(x - i) == 0 and abs(y - j) == 1):
                    possible_moves.add((i, j))

        return possible_moves



class Bishop():
    
    def __init__():
        pass


class Rook():
    
    def __init__():
        pass

class Queen():
    
    def __init__():
        pass


class Cells():

    def __init__(self, cell_size, position, object):

        self.x = position[0] * cell_size
        self.y = position[1] * cell_size
        self.coord = position

        self.cell_size = cell_size
        self.cell = pygame.Rect(self.x, self.y, self.cell_size, self.cell_size)

        self.object = object

    def draw_cell(self, colour, colour2, x, y, board):

            if self.x <= x <= self.x + self.cell_size and self.y <= y <= self.y + self.cell_size:
                pygame.draw.rect(screen, GREEN, self.cell)
            else:
                if ((self.x + self.y) // self.cell_size) % 2 == 0:
                    pygame.draw.rect(screen, colour, self.cell)
                else:
                    pygame.draw.rect(screen, colour2, self.cell)

            if "M" in self.object:
                surface = pygame.Surface((self.cell_size + 1, self.cell_size + 1), pygame.SRCALPHA)
                surface.fill((255, 0, 0, 140))
                screen.blit(surface, (self.x, self.y))

            if "N" in self.object:
                knight = Knight(self)
                knight.draw_knight()

            if "P" in self.object:
                player = Player(self)
                player.draw_player()


class Boards():

    def __init__(self, board):

        self.grid_size = self.width, self.height = len(board[0]), len(board)
        self.board_array = board

        # Generate cells
        self.cell_size = height / self.height
        self.cells = list()
        for i in range(self.width):
            for j in range(self.height):
                cell = Cells(self.cell_size, (i, j), board[j][i])
                self.cells.append(cell)

    def draw_board(self, x, y):

        for cell in self.cells:
            cell.draw_cell(DARK_GREEN, MID_GREEN, x, y, self.board_array)

        

class Buttons():

    def __init__(self, text, font_colour, button_size, position, font_size, button_colour, button_colour2):

        self.button_colour = button_colour
        self.button_colour2 = button_colour2
        self.text = text

        self.width = button_size[0]
        self.height = button_size[1]
        self.area = self.width * self.height
        self.font_size = font_size

        self.x = position[0]
        self.y = position[1]

        self.font = pygame.font.SysFont("arialblack", font_size)

        self.text_surface = self.font.render(text, True, font_colour)
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw_button(self, x, y):
        if self.button.x <= x <= self.button.x + self.width and self.button.y <= y <= self.button.y + self.height:
            pygame.draw.rect(screen, self.button_colour2, self.button)
            screen.blit(self.text_surface, (self.x, self.y + self.font_size * 0.4))
        else:
            pygame.draw.rect(screen, self.button_colour, self.button)
            screen.blit(self.text_surface, (self.x, self.y + self.font_size * 0.4))

        
class draw_background():

    def __init__(self):
        self.menu = pygame.image.load(os.path.join("Assets", "Images", "Title3.webp"))
        self.menu = pygame.transform.scale(self.menu, resolution)

    def Title(self):
        '''
        Title screen upon which the player first enters
        '''
        run = True
        # Main game loop
        while run:
            # Event handling
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Click registration
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit.button.collidepoint(event.pos):
                        quit.quit()
                    if level_editor.button.collidepoint(event.pos):
                        self.Level_editor()
                        run = False

            # Draw title screen
            screen.blit(self.menu, (0, 0))

            # Create buttons
            button_size = 800, 100

            quit = Buttons("Quit", WHITE, button_size, (width // 2 - button_size[0] // 2, 900), 50, GREY, BLACK)
            settings = Buttons("Settings", WHITE, button_size, (width // 2 - button_size[0] // 2, 900 - button_size[1]), 50, GREY, BLACK)
            level_editor = Buttons("Level Editor", WHITE, button_size, (width // 2 - button_size[0] // 2, 900 - button_size[1] * 2), 50, GREY, BLACK)
            continue_game = Buttons("Continue game", WHITE, button_size, (width // 2 - button_size[0] // 2, 900 - button_size[1] * 3), 50, GREY, BLACK)
            new_game = Buttons("New game", WHITE, button_size, (width // 2 - button_size[0] // 2, 900 - button_size[1] * 4), 50, GREY, BLACK)

            # Display buttons
            x, y = pygame.mouse.get_pos()
            
            quit.draw_button(x, y)
            settings.draw_button(x, y)
            level_editor.draw_button(x, y)
            continue_game.draw_button(x, y)
            new_game.draw_button(x, y)

            pygame.display.update()
            clock.tick(fps)

    def Pause_game(self):
        pass

    def Play_level(self, board):
        '''
        Allow user to playtest level in level editor
        '''
        run = True
        # Main game loop
        while run:
            # Event handling
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Click registration
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if cell is clicked on
                    for cell in board.cells:
                        if cell.cell.collidepoint(event.pos):

                            if "M" in cell.object:
                                new_board = board.board_array
                                for piece in PIECES:
                                    new_board[cell.coord[1]][cell.coord[0]] = new_board[cell.coord[1]][cell.coord[0]].replace(piece, "")
                                new_board[cell.coord[1]][cell.coord[0]] = new_board[cell.coord[1]][cell.coord[0]] + "P"
                                new_board[current.coord[1]][current.coord[0]] = new_board[current.coord[1]][current.coord[0]].replace("P", "")
                                board = Boards(new_board)
                            
                            # Remove highlighted cells
                            new_board = board.board_array
                            for i in range(len(new_board)):
                                for j in range(len(new_board[i])):
                                    if "M" in new_board[i][j]:
                                        new_board[i][j] = new_board[i][j].replace("M", "")
                            board = Boards(new_board)

                            if "P" in cell.object:
                                new_board = board.board_array
                                for move in Player.moves(board.board_array, (cell.coord)):
                                    new_board[move[1]][move[0]] = new_board[move[1]][move[0]] + "M"
                                board = Boards(new_board)
                                current = cell
            
            x, y = pygame.mouse.get_pos()

            screen.fill(DARK_GREEN)
            board.draw_board(x, y)

            pygame.display.update()
            clock.tick(fps)


    def Level_editor(self):
        '''
        Brings player to the level editor where the user can create their own levels.
        '''
        board = Boards([['#' for i in range(22)] for j in range(16)])
        run = True
        # Main game loop
        while run:
            # Event handling
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Click registration
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # Button operations
                    if save_level.button.collidepoint(event.pos):
                        Load_Save.save_level(board.board_array, "1")

                    if load_level.button.collidepoint(event.pos):
                        board = Boards(Load_Save.load_level(os.path.join("Levels", "User Levels", "1")))

                    if play_level.button.collidepoint(event.pos):
                        self.Play_level(board)
                        run = False

                # Key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.Pause_game()
                        
            
            screen.fill(DARK_GREEN)
            x, y = pygame.mouse.get_pos()

            board.draw_board(x, y)

            tab = pygame.Rect(board.cell_size * 22, 0, width - board.cell_size * 22, height)
            pygame.draw.rect(screen, GREY, tab)

            # Create buttons
            save_level = Buttons("Save Level", WHITE, (200, 40), (1520, 1020), 20, RED, DARK_RED)
            load_level = Buttons("Load Level", WHITE, (200, 40), (1520, 970), 20, RED, DARK_RED)
            play_level = Buttons("Play Level", WHITE, (150, 150), (1750, 900), 20, RED, DARK_RED)

            # Draw buttons
            save_level.draw_button(x, y)
            load_level.draw_button(x, y)
            play_level.draw_button(x, y)

            pygame.display.update()
            clock.tick(fps)

if __name__ == "__main__":
    current = draw_background()
    current.Title()