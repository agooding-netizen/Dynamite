from dynabot import *

gamestate = {}
gamestate['rounds'] = {}
game_round = {}
counter = 0
counter_water = 0
bot1 = DynaBot()
bot2 = DynaBot()

for i in range(0, 1000):
    game_round = {"p1": bot1.make_move(gamestate), "p2": bot2.make_move(gamestate)}
    if game_round['p1'] == 'D':
        counter += 1
    if game_round['p2'] == 'W':
        counter_water += 1
    gamestate['rounds'][0] = game_round
    print(game_round['p1'] + ' ' + game_round['p2'])

print(counter)
print(counter_water)