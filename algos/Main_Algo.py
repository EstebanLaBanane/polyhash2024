import game
from .Diriger_Ballon import  Points_Centre_Bloc
from game import Game
from random     import *
import map

#un dictionnaire globale sous forme de idBallon : coord [34,32]
from .distance_cells import distance_cells

global dict_ancienne_pos
global ballon_vers_centre
ballon_vers_centre={}
dict_ancienne_pos={}



def trouver_cle_par_valeur(dictionnaire, valeur_recherchee):
    for cle, valeur in dictionnaire.items():
        if valeur == valeur_recherchee:
            return cle
    return None

def attribuer_centre_unique(ballon, liste_centres_bloc):
    global ballon_vers_centre
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
    cov_r = g.balloons[0].coverage_radius
    row_map=g.game_map.rows
    col_map=g.game_map.cols
    zone_eff = (2 * cov_r + 1) ** 2
    row_eff = (zone_eff) ** (1 / 2)
    col_eff = (zone_eff) ** (1 / 2)
    for ballon in g.balloons:
<<<<<<< HEAD

        #possible de regler l'assignation juste dans ce bloc
        #probleme ici
        if ballon.balloon_id not in ballon_vers_centre.keys():
            #if len(liste_centres_bloc)==1:
            #    attribuer_centre(ballon, liste_centres_bloc)
            #else :
            zone_assigne=dictBallonZone[ballon.balloon_id]
            bloc_destination=MapBloc[zone_assigne]
            liste_centres_bloc=Points_Centre_Bloc(bloc_destination, row_eff, col_eff, row_map, col_map)
            attribuer_centre(ballon,liste_centres_bloc)

            print(liste_centres_bloc)
            print(ballon_vers_centre)
        #aller vers le centre
        #pour  altitude en 0 et 1 et -1 on met la distance entre la nouvelle cellule du ballon et target
        Liste_alt={}
        #probleme ici
        #cas sol : monter
        if ballon.altitude==0:
            action=1
        #cas pres du sol : monter ou rester
        elif ballon.altitude-1==0:
            #cas rester
            wind_to_apply = ballon.cell.get_wind(ballon.altitude)
            current_cell_col = ballon.cell.col
            current_cell_row = ballon.cell.row
            new_row = current_cell_row + wind_to_apply[0]
            new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
            print("row,col:",[new_row,new_col])
            #deadcell renvoit dict id : [safe,killer,safe,safe] altitude courante = altitude-1
            if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude-1] == 'safe':
                if wind_to_apply==[0,0]:
                    Liste_alt[ballon.altitude] = float('inf')
                else:
                    dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                    Liste_alt[ballon.altitude] = dist
            else:
                Liste_alt[ballon.altitude] = float('inf')
            #cas monter
            wind_to_apply = ballon.cell.get_wind(ballon.altitude+1)
            current_cell_col = ballon.cell.col
            current_cell_row = ballon.cell.row
            new_row = current_cell_row + wind_to_apply[0]
            new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
            print("row,col:",[new_row, new_col])
            if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude] == 'safe':
                dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                Liste_alt[ballon.altitude+1] = dist
            else:
                Liste_alt[ballon.altitude+1]=float('inf')
            #choisir l'altitude à prendre
            dist_min=min(Liste_alt.values())
            print(dist_min)
            alt_min=trouver_cle_par_valeur(Liste_alt,dist_min)
            if ballon.altitude==alt_min:
=======
        #on commence par voir si on est dans le tour de random du debut:
        if g.turns != g.max_turn and g.turns > g.max_turn-2:
            if not ballon.is_alive:
>>>>>>> 557ec586951b60a984e1845913f87ebaed41c0e4
                action = 0
            elif ballon.altitude <= 1:
                action = randint(0, 1)
            elif ballon.altitude == g.game_map.nb_altitudes:
                action = randint(-1, 0)
            else:
                action = randint(-1, 1)
            instructions.append(action)
        else:

            if ballon.is_alive==False:
                print("ballon mort")
                instructions.append(0)
            else:
                zone_assigne=dictBallonZone[ballon.balloon_id]
                bloc_destination=MapBloc[zone_assigne]
                liste_centres_bloc=Points_Centre_Bloc(bloc_destination, row_eff, col_eff, row_map, col_map)
                #possible de regler l'assignation juste dans ce bloc
                #probleme ici
                if ballon.balloon_id not in ballon_vers_centre.keys():
                    #if len(liste_centres_bloc)==1:
                    #    attribuer_centre(ballon, liste_centres_bloc)
                    #else :
                    attribuer_centre_unique(ballon,liste_centres_bloc)

                    print(liste_centres_bloc)
                    print(ballon_vers_centre)
                #aller vers le centre
                #pour  altitude en 0 et 1 et -1 on met la distance entre la nouvelle cellule du ballon et target
                Liste_alt={}
                #probleme ici
                #cas sol : monter
                if ballon.altitude==0:
                    action=1
                    ballon.memoire_positions.append([ballon.cell.row,ballon.cell.col,ballon.altitude])
                    print(ballon.memoire_positions)
                #cas pres du sol : monter ou rester
                elif ballon.altitude-1==0:
                    #cas rester

                    wind_to_apply = ballon.cell.get_wind(ballon.altitude)
                    current_cell_col = ballon.cell.col
                    current_cell_row = ballon.cell.row
                    new_row = current_cell_row + wind_to_apply[0]
                    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
                    print("row,col:",[new_row,new_col])
                    #deadcell renvoit dict id : [safe,killer,safe,safe] altitude courante = altitude-1
                    if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude-1] == 'safe':
                        if wind_to_apply==[0,0]:
                            Liste_alt[ballon.altitude] = float('inf')
                        else:
                            dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                            Liste_alt[ballon.altitude] = dist
                    else:
                        Liste_alt[ballon.altitude] = float('inf')
                    #cas monter
                    wind_to_apply = ballon.cell.get_wind(ballon.altitude+1)
                    current_cell_col = ballon.cell.col
                    current_cell_row = ballon.cell.row
                    new_row = current_cell_row + wind_to_apply[0]
                    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
                    print("row,col:",[new_row, new_col])
                    if len(ballon.memoire_positions)>=3 and ballon.memoire_positions[len(ballon.memoire_positions)-1]==ballon.memoire_positions[len(ballon.memoire_positions)-3]:
                        action = randint(0, 1)
                    else:

                        if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude] == 'safe':
                            dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                            Liste_alt[ballon.altitude+1] = dist
                        else:
                            Liste_alt[ballon.altitude+1]=float('inf')
                        #choisir l'altitude à prendre
                        dist_min=min(Liste_alt.values())
                        print(dist_min)
                        alt_min=trouver_cle_par_valeur(Liste_alt,dist_min)
                        if ballon.altitude==alt_min:
                            action = 0
                        elif ballon.altitude<alt_min:
                            action= 1
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col,ballon.altitude])
                    print(ballon.memoire_positions)
                    print(Liste_alt)
                    print("on est à l'alt:", ballon.altitude)
                    #print("il faut prendre l'altitude :", alt_min)

                #cas pres du max altitude : descendre ou rester
                elif ballon.altitude==g.game_map.nb_altitudes:
                    # cas rester
                    wind_to_apply = ballon.cell.get_wind(ballon.altitude)
                    print("ballon id:",ballon.balloon_id)
                    print("alt:",ballon.altitude)
                    print(wind_to_apply)
                    current_cell_col = ballon.cell.col
                    current_cell_row = ballon.cell.row
                    new_row = current_cell_row + wind_to_apply[0]
                    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
                    print("new_row,new_col:",[new_row, new_col])
                    #depassement de la map
                    if ballon.altitude-1>0:
                        if deadcells[g.game_map.cells[current_cell_row][current_cell_col].id][ballon.altitude-1] == 'safe':
                            if wind_to_apply==[0,0]:
                                Liste_alt[ballon.altitude] = float('inf')
                            else:
                                dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                                Liste_alt[ballon.altitude] = dist
                        else:
                            Liste_alt[ballon.altitude] = float('inf')
                    else:
                        Liste_alt[ballon.altitude] = float('inf')
                    # cas descendre
                    wind_to_apply = ballon.cell.get_wind(ballon.altitude - 1)
                    current_cell_col = ballon.cell.col
                    current_cell_row = ballon.cell.row
                    new_row = current_cell_row + wind_to_apply[0]
                    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
                    print("row,col:",[new_row, new_col])
                    #il faut reprogrammer deadcells
                    if len(ballon.memoire_positions)>=3 and ballon.memoire_positions[len(ballon.memoire_positions)-1]==ballon.memoire_positions[len(ballon.memoire_positions)-3]:
                        action = randint(0, 1)
                    else:
                        if ballon.altitude - 1 > 0 :
                            if deadcells[g.game_map.cells[current_cell_row][current_cell_col].id][ballon.altitude - 1] == 'safe':
                                dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                                Liste_alt[ballon.altitude - 1] = dist
                            else:
                                Liste_alt[ballon.altitude - 1] = float('inf')
                        else:
                            Liste_alt[ballon.altitude - 1] = float('inf')
                        # choisir l'altitude à prendre
                        dist_min = min(Liste_alt.values())
                        alt_min=trouver_cle_par_valeur(Liste_alt,dist_min)
                        if ballon.altitude == alt_min:
                            action = 0
                        elif ballon.altitude > alt_min:
                            action = - 1
                    print(Liste_alt)
                    print("on est à l'alt:", ballon.altitude)
                    #print("il faut prendre l'altitude :", alt_min)
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col,ballon.altitude])
                    print(ballon.memoire_positions)
                #rester descendre ou monter
                else:
                    # cas rester

                    wind_to_apply = ballon.cell.get_wind(ballon.altitude)
                    current_cell_col = ballon.cell.col
                    current_cell_row = ballon.cell.row
                    new_row = current_cell_row + wind_to_apply[0]
                    new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
                    print("row,col:",[new_row, new_col])
                    if len(ballon.memoire_positions)>=3 and ballon.memoire_positions[len(ballon.memoire_positions)-1]==ballon.memoire_positions[len(ballon.memoire_positions)-3]:
                        action = randint(-1,1)
                    else:
                        if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude-1] == 'safe':
                            if wind_to_apply==[0,0]:
                                Liste_alt[ballon.altitude] = float('inf')
                            else:
                                dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                                Liste_alt[ballon.altitude] = dist
                        else:
                            Liste_alt[ballon.altitude] = float('inf')
                        # cas monter
                        wind_to_apply = ballon.cell.get_wind(ballon.altitude + 1)
                        current_cell_col = ballon.cell.col
                        current_cell_row = ballon.cell.row
                        new_row = current_cell_row + wind_to_apply[0]
                        new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
                        print("row,col:",[new_row, new_col])
                        if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude] == 'safe':
                            dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                            Liste_alt[ballon.altitude + 1] = dist
                        else:
                            Liste_alt[ballon.altitude + 1] = float('inf')
                        # cas descendre
                        wind_to_apply = ballon.cell.get_wind(ballon.altitude - 1)
                        current_cell_col = ballon.cell.col
                        current_cell_row = ballon.cell.row
                        new_row = current_cell_row + wind_to_apply[0]
                        new_col = (current_cell_col + wind_to_apply[1]) % g.game_map.cols
                        print("row,col:",[new_row, new_col])
                        if deadcells[g.game_map.cells[new_row][new_col].id][ballon.altitude - 2] == 'safe':
                            dist = distance_cells([new_row, new_col], ballon_vers_centre[ballon.balloon_id])
                            Liste_alt[ballon.altitude - 1] = dist
                        else:
                            Liste_alt[ballon.altitude - 1] = float('inf')
                        # choisir l'altitude à prendre
                        dist_min = min(Liste_alt.values())
                        alt_min=trouver_cle_par_valeur(Liste_alt,dist_min)
                        if ballon.altitude == alt_min:
                            action = 0
                        elif ballon.altitude < alt_min:
                            action = 1
                        elif ballon.altitude > alt_min:
                            action = - 1
                    print(Liste_alt)
                    print("on est à l'alt:", ballon.altitude)
                    #print("il faut prendre l'altitude :", alt_min)
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col,ballon.altitude])
                    print(ballon.memoire_positions)
                print("action",action)
                instructions.append(action)
    return instructions

""" wind_to_apply = ballon.cell.get_wind(ballon.altitude)
        current_cell_col = ballon.cell.col
        current_cell_row = ballon.cell.row
        new_row = current_cell_row + wind_to_apply[0]
        new_col = (current_cell_col + wind_to_apply[1]) % self.game_map.cols"""
