"""
Assume only 2 players.
Ignore placement for third and fourth peice. Assume we only use 2 peices each.
More players and more peices will be considered later.
"""
class Board() # also used as State
    def __init__(self, init_loc = [[(2,2),(5,5)],[(2,5),(5,2)]]):
        self.width = 7
        self.height = 7
        self.players = 2 #player1 -> 0, player2 -> 1
        self.peices = 2
        self.peices_loc = init_loc # self.peices_loc[0][1] is location of first player's second peice
        self.hor_wall_loc = [[0 for _ in range(self.width)] for _ in range(self.height-1)]
        self.vert_wall_loc = [[0 for _ in range(self.width-1)] for _ in range(self.height)]
    
    def game_end(self):
        self.result = [[-1 for _ in range(self.width)] for _ in range(self.height)]
        self.game_ended = True
        for player in range(self.players):
            for peice_loc in peices_loc[player]:
                self.dfs(peice_loc, player)
        
        self.score = [0 for _ in range(self.players)]
        for player in range(self.players):
            for i in range(self.height):
                for j in range(self.width):
                    if self.result[i][j] == player:
                        self.score[player] += 1
        
        return self.game_ended, self.score

    def dfs(self, peice_loc, player):
        peice_r, peice_c = peice_loc
        if(self.result[peice_r][peice_c] == player)
            return
        elif(self.result[peice_r][peice_c] != -1)
            self.game_ended = False
            return
        self.result[peice_r][peice_c] = player
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for direction in dirs:
            dr, dc = direction
            if self.valid(peice_loc, direction):
                dfs((peice_r+dr, peice_c+dc), player)

    def valid(self, peice_loc, direction):
        peice_r, peice_c = peice_loc
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

    def place_hor_wall(self, wall_loc):
        wall_loc_r, wall_loc_c = wall_loc
        hor_wall_loc[wall_loc_r][wall_loc_c] = 1
    
    def place_vert_wall(self, wall_loc):
        wall_loc_r, wall_loc_c = wall_loc
        vert_wall_loc[wall_loc_r][wall_loc_c] = 1
    
    def move_piece(self, player, peice, peice_loc)
        