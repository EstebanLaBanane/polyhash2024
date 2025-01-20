from algos.cut_map import *
from map import Map
from algos.Decoupe_OPT import cut_map_optimise
from algos.score_of_cells2 import score_of_cells


def concentration_cells_pts(file_path):
    #initialisation
    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, vents_alt = read(file_path)
    game_map = Map(start_row, start_col, nb_row, nb_col, nb_alt, vents_alt, targets_pos)
    Maps=[]
    for elem in cut_map_optimise(file_path):
         Maps.append(elem)

    dict_cell_pts=score_of_cells(file_path)

    #calcule pour une map la concentration de points
    def concentration_par_map(mapcut: list, cell_pt: dict, game_map: Map) -> int:
        score = 0
        for i in range(len(mapcut)):
            row_cell, col_cell = mapcut[i][0], mapcut[i][1]
            cellrecherche = game_map.get_cell(row_cell, col_cell)
            score += cell_pt[cellrecherche.id]
        return score
    #calcul de concentration de pt pour chaque partie de map
    dict_map_score={}
    for i in range(len(Maps)):
         dict_map_score[i]=concentration_par_map(Maps[i],dict_cell_pts,game_map)

    #output : dictionnaire avec id de la map et pourcentage de score qu'elle contient
    return dict_map_score


