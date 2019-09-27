
class DynaBot:
    def __init__(self):
        self.dynamite_count = 0
        self.opponent_dynamite_count = 0
        self.index = 0
        self.move_count = 0
        self.draw_count = 0
        self.round_count = 0
        self.points_count = 0

    def make_move(self, gamestate):
        if gamestate['rounds']:
            for game_round in gamestate['rounds']:
                if gamestate['rounds'][0]['p2'] == 'D':
                    self.opponent_dynamite_counter()
                if gamestate['rounds'][0]['p1'] == gamestate['rounds'][0]['p2']:
                    self.draw_counter()
        moves = ['R', 'P', 'S', 'D']
        move = moves[self.index]
        self.dynamite_counter(move)
        if self.draw_count == 2 and self.dynamite_count < 100:
            self.index = 3
            self.draw_count = 0
        else:
            self.index_counter(move, gamestate)
        self.move_counter()
        self.round_counter()
        return move

    def dynamite_counter(self, move):
        if move == 'D':
            self.dynamite_count += 1

    def opponent_dynamite_counter(self):
        self.opponent_dynamite_count += 1

    def move_counter(self):
        self.move_count += 1

    def draw_counter(self):
        self.draw_count += 1

    def index_counter(self, move, gamestate):
        if self.dynamite_count < 100:
            self.index = hash(hex(id(move)) + str(gamestate)) % 4
        # elif self.opponent_dynamite_count < 100:
        #     self.index = hash(hex(id(move)) + str(gamestate)) % 4
        else:
            self.index = hash(hex(id(move)) + str(gamestate)) % 3

    def round_counter(self):
        self.round_count += 1

    def points_available_counter(self):
        points_available = self.draw_count + 1
        return points_available

    def points_counter(self, result):
        if result == "Win":
            self.points_count += self.points_available_counter()


