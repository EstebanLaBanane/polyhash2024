import game
from .Diriger_Ballon import  Points_Centre_Bloc
from game import Game
from random     import *
import map

#un dictionnaire globale sous forme de idBallon : coord [34,32]
from .distance_cells import distance_cells
#global dictBallonZone
global dict_id_cycle
global dict_ancienne_pos
global liste_eviter
global ballon_vers_centre
global deja_choisi
#dictBallonZone={}
ballon_vers_centre={}
dict_ancienne_pos={}
dict_id_cycle={}
liste_eviter=[]
deja_choisi=[]

def contient_doublons(liste):
    vus = set()
    for element in liste:
        if isinstance(element, list):
            element = tuple(element)
        if element in vus:
            return True
        vus.add(element)
    return False

def move(ballon,Liste_alt,g,deadcells,cas):
    wind_to_apply = ballon.cell.get_wind(ballon.altitude+cas)
    current_cell_col = ballon.cell.col
    current_cell_row = ballon.cell.row
    new_row = current_cell_row + wind_to_apply[0]
    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
    print("row,col:", [new_row, new_col])
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

def filtrage(liste_eviter:list,deja_choisi:list):
    for elem in deja_choisi:
        if elem in liste_eviter:
            deja_choisi.remove(elem)


#Pointscentrebloc
def Main_Algo(g:Game,MapBloc,dictBallonZone,deadcells)->list[int]:
    global ballon_vers_centre
    #global dictBallonZone
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
            # 3 solutions pour cycle : 1 random, 2 deuxieme dist, 3 attribuer centre
            if ballon.is_alive == False:
                print("ballon mort")
                instructions.append(0)
            else:
                centre_sans_cycle = 0
                zone_assigne = dictBallonZone[ballon.balloon_id]
                bloc_destination = MapBloc[zone_assigne]
                liste_centres_bloc = Points_Centre_Bloc(bloc_destination, row_eff, col_eff, row_map, col_map)
                print(liste_centres_bloc)
                Liste_alt = {}
                #si on fait 10 tours on efface la mémoire
                i=30
                if g.turns%i==0:
                    ballon.memoire_positions.clear()

                if ballon.balloon_id not in ballon_vers_centre.keys():
                    if [ballon.cell.row, ballon.cell.col] in bloc_destination:
                        if attribuer_centre_unique(ballon, liste_centres_bloc) != None:
                            attribuer_centre_unique(ballon, liste_centres_bloc)
                        else:
                            attribuer_centre(ballon, liste_centres_bloc)
                    else:
                        attribuer_centre(ballon, liste_centres_bloc)

                # initialisation
                if ballon.balloon_id not in dict_id_cycle:
                        dict_id_cycle[ballon.balloon_id] = False

                # lorsque le dictionnaire est complet et on atteint un nb_ntour
                print(g.turns)


                #pendant 20 tours on fait les attributions
                if (dict_id_cycle[ballon.balloon_id] == True) and (len(dict_id_cycle) == len(g.balloons) ) and (g.max_turn - 60<=g.turns <= (g.max_turn - 40)): #40
                    filtrage(liste_eviter,deja_choisi)
                    for k in dict_id_cycle:
                        if dict_id_cycle[k] == False and (k not in liste_eviter) and (k not in deja_choisi):
                            dict_id_cycle[ballon.balloon_id] = False
                            deja_choisi.append(k)
                            break

                    print(centre_sans_cycle)
                    print(liste_centres_bloc)

                # attribuer_centre(ballon, liste_centres_bloc)
                #print(centre_sans_cycle)
                if deja_choisi!=[] and dict_id_cycle[ballon.balloon_id] == True:
                    centre_sans_cycle=choice(deja_choisi)
                    zone_assigne = dictBallonZone[centre_sans_cycle]
                    bloc_destination = MapBloc[zone_assigne]
                    liste_centres_bloc = Points_Centre_Bloc(bloc_destination, row_eff, col_eff, row_map, col_map)

                print("dict_ballon_zone",dictBallonZone)
                print("a eviter:",liste_eviter)
                print("deja choisi",deja_choisi)
                print("dict_id_cycle:", dict_id_cycle)
                print("balon id :",ballon.balloon_id)
                print("turns :",g.turns)
                print(liste_centres_bloc)
                print(ballon_vers_centre)
                # aller vers le centre
                # pour  altitude en 0 et 1 et -1 on met la distance entre la nouvelle cellule du ballon et target

                # probleme ici
                # cas sol : monter
                if ballon.altitude == 0:
                    action = 1
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col, ballon.altitude])
                    print(ballon.memoire_positions)
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
                    if len(ballon.memoire_positions) >= 3 and contient_doublons(ballon.memoire_positions):
                        dict_id_cycle[ballon.balloon_id] = True
                        if ballon.balloon_id not in liste_eviter:
                            liste_eviter.append(ballon.balloon_id)
                        ballon.memoire_positions = []
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col, ballon.altitude])
                    print(Liste_alt)
                    print("on est à l'alt:", ballon.altitude)
                    print("il faut prendre l'altitude :", alt_min)

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
                    if len(ballon.memoire_positions) >= 3 and contient_doublons(ballon.memoire_positions):
                        dict_id_cycle[ballon.balloon_id] = True
                        if ballon.balloon_id not in liste_eviter:
                            liste_eviter.append(ballon.balloon_id)
                        print(ballon.memoire_positions)
                        ballon.memoire_positions = []
                    print(Liste_alt)
                    print("on est à l'alt:", ballon.altitude)
                    print("il faut prendre l'altitude :", alt_min)
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col, ballon.altitude])
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

                    if len(ballon.memoire_positions) >= 3 and contient_doublons(ballon.memoire_positions):
                        dict_id_cycle[ballon.balloon_id] = True
                        if ballon.balloon_id not in liste_eviter:
                            liste_eviter.append(ballon.balloon_id)
                        print(ballon.memoire_positions)
                        ballon.memoire_positions = []
                    print(Liste_alt)
                    print("on est à l'alt:", ballon.altitude)
                    print("il faut prendre l'altitude :", alt_min)
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col, ballon.altitude])
        print("action", action)
        instructions.append(action)
    return instructions

