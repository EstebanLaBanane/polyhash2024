from read_input import read


def cut_map(filepath):
    #on recupere la lecture des données

    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, formatted_vent = read(filepath)

    #on crée la map sous forme de list[list[int]]

    map = []
    for row in range(nb_row):
        for col in range(nb_col):
            map.append([row, col])

    #sous fonction qui coupe la map sur deux sur l'axe y

    def cut_col():
        half_map_row_left=[]
        half_map_row_right=[]
        for row in range(nb_row):
            for col in range(nb_col//2):
                half_map_row_left.append([row, col])
        for row in range(nb_row):
            for col in range(nb_col // 2,nb_col):
                half_map_row_right.append([row, col])
        return half_map_row_left, half_map_row_right

    #sous fonction qui coupe la map sur deux sur l'axe x

    def cut_row():
        half_map_row_left = []
        half_map_row_right = []
        for row in range(nb_row//2):
            for col in range(nb_col ):
                half_map_row_left.append([row, col])
        for row in range(nb_row//2,nb_row):
            for col in range(nb_col ):
                half_map_row_right.append([row, col])
        return half_map_row_left, half_map_row_right

    #on recupere toutes les coupes de map qu'on crée avec les sous fonctions

    half_map_col_left, half_map_col_right = cut_col()
    half_map_row_left, half_map_row_right = cut_row()




    return half_map_col_left, half_map_col_right, half_map_row_left, half_map_row_right




