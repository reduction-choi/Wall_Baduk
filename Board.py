"""
Assume only 2 players.
Ignore placement for third and fourth peice. Assume we only use 2 peices each.
More players and more peices will be considered later.
"""
class Board() # also used as State
    def __init__(self, init_loc = [[(2,2),(5,5)],[(2,5),(5,2)]]):
        self.width = 7
        self.height = 7
        self.players = 2
        self.peices = 2
        self.peice_loc = init_loc # self.peice_loc[0][1] is location of first player's second peice
        self.hor_wall_loc = [[0 for _ in range(self.width)] for _ in range(self.height-1)]
        self.vert_wall_loc = [[0 for _ in range(self.width-1)] for _ in range(self.height)]
    
    def is_game_end(self):
        self.result = [[-1 for _ in range(self.width)] for _ in range(self.height)]
        self.game_ended = True
        for player in range(self.players):
            for peice in range(self.peices):
                self.dfs(peice_loc[player][peice], player)

    def dfs(self, peice, player):
        peice_r, peice_c = peice
        if(self.result[peice_r][peice_c] == player)
            return
        elif(self.result[peice_r][peice_c] != -1)
            self.game_ended = False
            return
        self.result[peice_r][peice_c] = player
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for direction in dirs:
            dr, dc = direction
            if self.valid(peice, direction):
                dfs((peice_r+dr, peice_c+dc), player)

    def valid(self, peice, direction):
        peice_r, peice_c = peice
        dr, dc = direction
        if peice_r < 0  or peice_r > self.height:
            return False
        if peice_c < 0 or peice_c > self.width:
            return False
        if dr == 1 and self.hor_wall_loc[peice_r][peice_c] == 1:
            return False
        if dr == -1 and self.hor_wall_loc[peice_r-1][peice_c] == 1:
            return False
        if dc == 1 and self.vert_wall_loc[peice_r][peice_c] == 1:
            return False
        if dc == -1 and self.vert_wall_loc[peice_r][peice_c-1] == 1:
            return False
        return True

    def 