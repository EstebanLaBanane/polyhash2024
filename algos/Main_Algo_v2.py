import game
from .Diriger_Ballon import  Points_Centre_Bloc
from game import Game
from random     import *
import map

#un dictionnaire globale sous forme de idBallon : coord [34,32]
from .distance_cells import distance_cells
import json
from pathlib import Path

# Variables globales
global dictBallonZoneCopie
global ballon_vers_centre
global liste_eviter
global deja_choisi
global dict_id_cycle

# Initialisation des variables
dictBallonZoneCopie = {}
ballon_vers_centre = {}
dict_id_cycle = {}
liste_eviter = []
deja_choisi = []

# Fichier pour sauvegarder les variables globales
SAVE_FILE = "globals_state.json"

#permet la sauvegarde des données même après la fermeture du fichier
def sauvegarder_etat():
    """Sauvegarde l'état des variables globales dans un fichier JSON."""
    etat = {
        "dictBallonZoneCopie": dictBallonZoneCopie,
        "ballon_vers_centre": ballon_vers_centre,
        "liste_eviter": liste_eviter,
        "a_choisir": a_choisir,
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(etat, f)
    print("État sauvegardé.")

def charger_etat():
    """Charge l'état des variables globales depuis un fichier JSON."""
    global dictBallonZoneCopie, ballon_vers_centre, liste_eviter, a_choisir

    if Path(SAVE_FILE).exists():
        with open(SAVE_FILE, "r") as f:
            etat = json.load(f)
            dictBallonZoneCopie = etat.get("dictBallonZoneCopie", {})
            ballon_vers_centre = etat.get("ballon_vers_centre", {})
            liste_eviter = etat.get("liste_eviter", [])
            a_choisir = etat.get("a_choisir", [])
        print("État chargé.")
    else:
        print("Aucun état précédent trouvé. Initialisation avec des valeurs par défaut.")

# Appel du chargement au démarrage
charger_etat()

#permet de savoir si il y a des doublons dans une liste
def contient_doublons(liste):
    vus = set()
    for element in liste:
        if isinstance(element, list):
            element = tuple(element)
        if element in vus:
            return True
        vus.add(element)
    return False

#prend la decision dans le choix de quelle altitude prendre
def prise_de_decision(Liste_alt,ballon):
    dist_min = min(Liste_alt.values())
    alt_min = trouver_cle_par_valeur(Liste_alt, dist_min)
    if ballon.altitude == alt_min:
        action = 0
    elif ballon.altitude < alt_min:
        action = 1
    elif ballon.altitude > alt_min:
        action = - 1
    return action

#calcul de distance entre ballon et destination dans les differentes altitudes
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

#permet de trouver la cle à travers la valeur
def trouver_cle_par_valeur(dictionnaire, valeur_recherchee):
    for cle, valeur in dictionnaire.items():
        if valeur == valeur_recherchee:
            return cle
    return None

#attribue un centre unique au ballon
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


#attribue un centre d'index 0 de la liste des centres au ballon
def attribuer_centre(ballon,liste_centres_bloc):
    global ballon_vers_centre
    if  isinstance(liste_centres_bloc,list) and all(isinstance(x, int) for x in liste_centres_bloc) and len(liste_centres_bloc) == 2:
        centre = liste_centres_bloc
    else:
        centre=liste_centres_bloc[0]
    if isinstance(centre,list) and all(isinstance(x, int) for x in centre) and len(centre) == 2:
        ballon_vers_centre[ballon.balloon_id] = centre

#fonction qui permet d'eliminer les element present dans la liste deja_choisi present dans liste_eviter
def filtrage(liste_eviter, deja_choisi):
    return [elem for elem in deja_choisi if elem not in liste_eviter]

#fonction qui permet de detecter si un ballon est dans un cycle
def detection_de_cycle(ballon):
    if len(ballon.memoire_positions) >= 3 and contient_doublons(ballon.memoire_positions):
        if ballon.balloon_id not in liste_eviter:
            liste_eviter.append(ballon.balloon_id)
        ballon.memoire_positions = []

#attribue au ballon un centre
def attribution_centre(ballon,liste_centres_bloc):
    if ballon.balloon_id not in ballon_vers_centre.keys():
        if attribuer_centre_unique(ballon, liste_centres_bloc) != None:
            attribuer_centre_unique(ballon, liste_centres_bloc)
        else:
            attribuer_centre(ballon, liste_centres_bloc)

#lance les ballons aleatoirement
def mode_random(ballon,g):
    if not ballon.is_alive:
        action = 0
    elif ballon.altitude <= 1:
        action = randint(0, 1)
    elif ballon.altitude == g.game_map.nb_altitudes:
        action = randint(-1, 0)
    else:
        action = randint(-1, 1)
    return action

#elimine les doublons d'une liste
def eliminer_doublons(liste):
    vus = set()
    liste_sans_doublons = []
    for element in liste:
        if element not in vus:
            liste_sans_doublons.append(element)
            vus.add(element)
    return liste_sans_doublons



def Main_Algo_v2(g:Game,MapBloc,dictBallonZone,deadcells)->list[int]:
    global dictBallonZoneCopie, ballon_vers_centre,  liste_eviter, deja_choisi, dict_id_cycle
    instructions=[]
    action=float('inf')
    cov_r = g.balloons[0].coverage_radius
    row_map=g.game_map.rows
    col_map=g.game_map.cols
    zone_eff = (2 * cov_r + 1) ** 2
    row_eff = (zone_eff) ** (1 / 2)
    col_eff = (zone_eff) ** (1 / 2)
    for ballon in g.balloons:
        #on copie le dict dictBallonZone
        if g.turns == (g.max_turn):
            dictBallonZoneCopie = dictBallonZone.copy()

        #dans les 10 premiers tours on lance les ballon aleatoirement pour une meilleur repartition
        if g.turns != g.max_turn and g.turns >= g.max_turn-10:
            action=mode_random(ballon,g)
        else:
            if ballon.is_alive == False:
                print("ballon mort")
                instructions.append(0)
            else:


                Liste_alt = {}
                #si on fait 20 tours on efface la mémoire des ballons pour eviter la confusion dans la detection des cycles
                i=20
                if g.turns%i==0:
                    ballon.memoire_positions.clear()


                # initialisation de dict_id_cyle
                if ballon.balloon_id not in dict_id_cycle:
                        dict_id_cycle[ballon.balloon_id] = False


                #à partir de 20 tours on remplis la liste deja_choisi : liste des centres à suivre
                if (dict_id_cycle[ballon.balloon_id] == True) and (len(dict_id_cycle) == len(g.balloons) ) and (g.turns <= (g.max_turn - 20)):
                    for k in dict_id_cycle:
                        if dict_id_cycle[k] == False and (k not in liste_eviter) and (k not in deja_choisi):
                            deja_choisi.append(k)
                            break

                #changement des centres pour les ballons dans un cycle
                filtrage(liste_eviter,deja_choisi)
                if ballon.balloon_id in liste_eviter:
                    if deja_choisi==[]:
                        pass
                    else:
                        centre_sans_cycle=choice(deja_choisi)
                        dictBallonZoneCopie[ballon.balloon_id] = dictBallonZoneCopie[centre_sans_cycle]
                        liste_eviter.remove(ballon.balloon_id)

                #assignation des centres
                zone_assigne = dictBallonZoneCopie[ballon.balloon_id]
                bloc_destination = MapBloc[zone_assigne]
                liste_centres_bloc = Points_Centre_Bloc(bloc_destination, row_eff, col_eff, row_map, col_map)
                attribution_centre(ballon, liste_centres_bloc)


                # cas sol : monter
                if ballon.altitude == 0:
                    action = 1
                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col, ballon.altitude])

                # cas pres du sol : monter ou rester
                elif ballon.altitude - 1 == 0:
                    # cas rester
                    cas=0
                    move(ballon,Liste_alt, g, deadcells, cas)
                    # cas monter
                    cas=1
                    move(ballon, Liste_alt, g, deadcells, cas)

                    # choisir l'altitude à prendre
                    action=prise_de_decision(Liste_alt, ballon)

                    #detection de cycle
                    detection_de_cycle(ballon)

                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col, ballon.altitude])

                # cas pres du max altitude : descendre ou rester
                elif ballon.altitude == g.game_map.nb_altitudes:
                    # cas rester
                    cas=0
                    move(ballon,Liste_alt,g,deadcells,cas)

                    # cas descendre
                    cas=-1
                    move(ballon,Liste_alt,g,deadcells,cas)

                    # choisir l'altitude à prendre
                    action=prise_de_decision(Liste_alt, ballon)

                    #detection de cycle
                    detection_de_cycle(ballon)

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
                    action=prise_de_decision(Liste_alt, ballon)

                    #detection de cycle
                    detection_de_cycle(ballon)

                    ballon.memoire_positions.append([ballon.cell.row, ballon.cell.col, ballon.altitude])

        instructions.append(action)
    if len(instructions)==len(g.balloons):
        return instructions
    else:
        return [0]*len(g.balloons)


import atexit
atexit.register(sauvegarder_etat)
