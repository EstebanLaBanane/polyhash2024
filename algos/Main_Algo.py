import game
from .Diriger_Ballon import  Points_Centre_Bloc
from game import Game
from random     import *
import map

#un dictionnaire globale sous forme de idBallon : coord [34,32]
from .distance_cells import distance_cells
global ballon_vers_centre
ballon_vers_centre={}


def move(ballon,Liste_alt,g,deadcells,cas):
    wind_to_apply = ballon.cell.get_wind(ballon.altitude+cas)
    current_cell_col = ballon.cell.col
    current_cell_row = ballon.cell.row
    new_row = current_cell_row + wind_to_apply[0]
    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
    if new_row < 0 or new_row >= g.game_map.rows:
        Liste_alt[ballon.altitude+cas] = float('inf')
    else:
        if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude+cas- 1] == 'safe':
            dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
            if wind_to_apply == [0, 0]:
                Liste_alt[ballon.altitude+cas] = float('inf')
            else:
                Liste_alt[ballon.altitude+cas] = dist
        else:
            Liste_alt[ballon.altitude+cas] = float('inf')


def trouver_cle_par_valeur(dictionnaire, valeur_recherchee):
    for cle, valeur in dictionnaire.items():
        if valeur == valeur_recherchee:
            return cle
    return None

def attribuer_centre_unique(ballon, liste_centres_bloc):
    global ballon_vers_centre
    centre=[]
    #type [int,int]
    if  isinstance(liste_centres_bloc,list) and all(isinstance(x, int) for x in liste_centres_bloc) and len(liste_centres_bloc) == 2:
        centre = liste_centres_bloc
    else:
    #type [[int,int],[int,int]...]
        for centre1 in liste_centres_bloc:
            if centre1 not in ballon_vers_centre.values():
                centre=centre1
                break
    if isinstance(centre,list) and all(isinstance(x, int) for x in centre) and len(centre) == 2:
        if centre==[]:
            return None
        else:
            ballon_vers_centre[ballon.balloon_id] = centre


def attribuer_centre(ballon,liste_centres_bloc):
    global ballon_vers_centre
    if  isinstance(liste_centres_bloc,list) and all(isinstance(x, int) for x in liste_centres_bloc) and len(liste_centres_bloc) == 2:
        centre = liste_centres_bloc
    else:
        centre=liste_centres_bloc[0]
    if isinstance(centre,list) and all(isinstance(x, int) for x in centre) and len(centre) == 2:
        ballon_vers_centre[ballon.balloon_id] = centre




#Pointscentrebloc
def Main_Algo(g:Game,MapBloc,dictBallonZone,deadcells)->list[int]:
    global ballon_vers_centre
    instructions=[]
    action=float('inf')
    cov_r = g.balloons[0].coverage_radius
    row_map=g.game_map.rows
    col_map=g.game_map.cols
    zone_eff = (2 * cov_r + 1) ** 2
    row_eff = (zone_eff) ** (1 / 2)
    col_eff = (zone_eff) ** (1 / 2)
    for ballon in g.balloons:
        #on commence par voir si on est dans le tour de random du debut:
        if g.turns != g.max_turn and g.turns > g.max_turn-10:
            if not ballon.is_alive:
                action = 0
            elif ballon.altitude <= 1:
                action = randint(0,1)
            elif ballon.altitude == g.game_map.nb_altitudes:
                action = randint(-1, 0)
            else:
                action = randint(-1, 1)
        else:
            if ballon.is_alive == False:
                print("ballon mort")
                action=0
            else:
                zone_assigne = dictBallonZone[ballon.balloon_id]
                bloc_destination = MapBloc[zone_assigne]
                liste_centres_bloc = Points_Centre_Bloc(bloc_destination, row_eff, col_eff, row_map, col_map)
                Liste_alt = {}


                if ballon.balloon_id not in ballon_vers_centre.keys():
                    if [ballon.cell.row, ballon.cell.col] in bloc_destination:
                        if attribuer_centre_unique(ballon, liste_centres_bloc) != None:
                            attribuer_centre_unique(ballon, liste_centres_bloc)
                        else:
                            attribuer_centre(ballon, liste_centres_bloc)
                    else:
                        attribuer_centre(ballon, liste_centres_bloc)


                # cas sol : monter
                if ballon.altitude == 0:
                    action = 1

                # cas pres du sol : monter ou rester
                elif ballon.altitude - 1 == 0:

                    # cas rester
                    cas=0
                    move(ballon,Liste_alt, g, deadcells, cas)

                    # cas monter
                    cas=1
                    move(ballon, Liste_alt, g, deadcells, cas)

                    # choisir l'altitude à prendre
                    dist_min = min(Liste_alt.values())
                    print(dist_min)
                    alt_min = trouver_cle_par_valeur(Liste_alt, dist_min)
                    if ballon.altitude == alt_min:
                        action = 0
                    elif ballon.altitude < alt_min:
                        action = 1


                # cas pres du max altitude : descendre ou rester
                elif ballon.altitude == g.game_map.nb_altitudes:
                    # cas rester
                    cas=0
                    move(ballon,Liste_alt,g,deadcells,cas)

                    # cas descendre
                    cas=-1
                    move(ballon,Liste_alt,g,deadcells,cas)

                    # choisir l'altitude à prendre
                    dist_min = min(Liste_alt.values())
                    alt_min = trouver_cle_par_valeur(Liste_alt, dist_min)
                    if ballon.altitude == alt_min:
                        action = 0
                    elif ballon.altitude > alt_min:
                        action = - 1


                # rester descendre ou monter
                else:
                    # cas rester
                    cas=0
                    move(ballon, Liste_alt, g, deadcells, cas)

                    # cas monter
                    cas = 1
                    move(ballon, Liste_alt, g, deadcells, cas)

                    # cas descendre
                    cas=-1
                    move(ballon, Liste_alt, g, deadcells, cas)

                    # choisir l'altitude à prendre
                    dist_min = min(Liste_alt.values())
                    alt_min = trouver_cle_par_valeur(Liste_alt, dist_min)
                    if ballon.altitude == alt_min:
                        action = 0
                    elif ballon.altitude < alt_min:
                        action = 1
                    elif ballon.altitude > alt_min:
                        action = - 1
        instructions.append(action)
    if len(instructions)==len(g.balloons):
        return instructions
    else:
        return [0]*len(g.balloons)


