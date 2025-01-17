from game       import Game
from random     import *

seed(3)

def check(ballon,g,action):
    wind_to_apply = ballon.cell.get_wind(ballon.altitude+action)
    current_cell_row = ballon.cell.row
    new_row = current_cell_row + wind_to_apply[0]
    print("new_row:",new_row)
    print("action associé:",action)
    if new_row < 0 or new_row >= g.game_map.rows:
        return False
    else:
        return True

#l'algo random optimisé est un algo random normale mais qui ne tue pas les ballons
#pour chaque tour il donne des instructions à tous les ballons
def rando_algo2(g : Game) -> list[int]:
    instruction = []
    limite=0
    for balloon in g.balloons:
        if not balloon.is_alive:
            action = 0
        #cas pres du sol
        elif balloon.altitude <= 1:
            action = randint(0,1)
            while(check(balloon,g,action)==False):
                action = randint(0, 1)
                #des fois on a pas le choix, le ballon est condamné
                if limite==20:
                    break
                limite+=1

        #cas pres du max altitude
        elif balloon.altitude==g.game_map.nb_altitudes:
            action = randint(-1,0)
            while (check(balloon, g, action) == False):
                action = randint(-1, 0)
                if limite==20:
                    break
                limite+=1
        #autre cas
        else:
            action = randint(-1,1)
            while (check(balloon, g, action) == False):
                action = randint(-1, 1)
                if limite==20:
                    break
                limite+=1
        print("action choisie:",action)
        instruction.append(action)

    return instruction

