from game       import Game
from random     import *

seed(3)

#pour chaque tour il donne des instructions à tous les ballons
def rando_algo(g : Game) -> list[int]:    
    instruction = []
    for balloon in g.balloons:
        if not balloon.is_alive:
            action = 0
        elif balloon.altitude <= 1:
            action = randint(0,1)
        elif balloon.altitude==g.game_map.nb_altitudes:
            action = randint(-1,0)
        else:
            action = randint(-1,1)
        instruction.append(action)

    return instruction