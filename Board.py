class Cell:
    def __init__():
        self.button = Button()
        self.piece = None

    def isempty(self):
        return self.piece == None

class Piece:
    def __init__():
        self.x = 0
        self.y = 0

    def setPosition(x, y):
        self.x = x
        self.y = y

class Wall:
    def __init__():
        self.horizontal = True
        self.x = 0
        self.y = 0

    def setPosition(x, y):
        self.x = x
        self.y = y

class Board:
    def __init__(size, players):
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.piece = [[Piece(), Piece()] for _ in range(players)]

    def isend(self):
        return False

    def move_piece(self):
        pass
    
    def place_wall(self):
        pass

    def calc(self):
        pass