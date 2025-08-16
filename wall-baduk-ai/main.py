from Board import *
class Wall_Baduk():
    def __init__(size):
        self.board = Board()
    
    def next_turn(self):
        self.turn++
        if self.turn > self.players:
            self.turn = 1
            
    def turn(self):
        self.board.move_piece(self.turn)
        self.board.place_wall(self.turn)

    def run(self):
        if self.board.isend():
            result()
        else:
            next_turn()
            turn()
    
    def select_positon(self, player):
        pass

    def select_starting_position(self):
        for i in range(self.players):
            self.select_positon(i+1)
        for i in range(self.players):
            self.select_positon(self.players + 1 - i)
    
    def start(self):
        self.select_starting_position()
        self.run()

if __name__ == '__main__':
    baduk = Wall_Baduk()
    baduk.start()