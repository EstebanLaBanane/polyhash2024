from game       import Game
from random     import *


seed(3)

def check(ballon,g,action,deadcells):
    wind_to_apply = ballon.cell.get_wind(ballon.altitude+action)
    current_cell_row = ballon.cell.row
    current_cell_col = ballon.cell.col
    new_row = current_cell_row + wind_to_apply[0]
    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
    if new_row < 0 or new_row >= g.game_map.rows:
        return False
    else:
        if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude + action - 1] == 'safe':
            return True
        else:
            return False

#l'algo random optimisé est un algo random normale mais qui ne tue pas les ballons
#pour chaque tour il donne des instructions à tous les ballons
def rando_algo2(g : Game,deadcells) -> list[int]:
    instruction = []
    #on met une limite de 20 pour voir si il y a une action qui tue pas quand on est dans une case
    limite=0
    for balloon in g.balloons:
        if not balloon.is_alive:
            action = 0
        #cas pres du sol
        elif balloon.altitude <= 1:
            action = randint(0,1)
            while(check(balloon,g,action,deadcells)==False):
                action = randint(0, 1)
                #des fois on a pas le choix, le ballon est condamné
                if limite==20:
                    break
                limite+=1

        #cas pres du max altitude
        elif balloon.altitude==g.game_map.nb_altitudes:
            action = randint(-1,0)
            while (check(balloon, g, action,deadcells) == False):
                action = randint(-1, 0)
                if limite==20:
                    break
                limite+=1

        #autre cas
        else:
            action = randint(-1,1)
            while (check(balloon, g, action,deadcells) == False):
                action = randint(-1, 1)
                if limite==20:
                    break
                limite+=1

        instruction.append(action)

    return instruction

