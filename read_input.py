

def read(filepath):
# Ouverture du fichier
    source = open(filepath)
# Lecture des données et séparation par ligne
    data = source.read().split('\n')
    data = data[:-1]

# Récupération des valeurs config
    nb_row, nb_col, nb_alt = data[0].split(' ')[:3]
    nb_tgt_cell, cov_r, nb_balloon, turns = data[1].split(' ')[:4]
    start_row, start_col = data[2].split(' ')[:2]
# Conversion en int
    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col = int(nb_row), int(nb_col), int(nb_alt) ,int(nb_tgt_cell) , int(cov_r), int(nb_balloon), int(turns), int(start_row), int(start_col)

# Récupération des positions des targets
# Conversion en int
    targets_pos = []
    for i in range (3,3+nb_tgt_cell):
        target_pos_str = data[i].split(' ')[:2]
        target_pos_int = [int(pos) for pos in target_pos_str]
        targets_pos.append(target_pos_int)

# Séparation des vents par altitude
# Conversion en int
    vents_altitudes = []
    indice_debut_vents = 3+nb_tgt_cell

    for i in range(nb_alt):
        vents_altitudes.append(data[indice_debut_vents+i*nb_alt:indice_debut_vents+i*nb_alt+nb_row])

    formatted_vent = []
    for _ in range(nb_alt):
        formatted_vent.append([])

    counter = -1

    for vents_alt in vents_altitudes:
        counter+=1
        for vents_alt_row in vents_alt:
            vents_alt_row = vents_alt_row.split(' ')
            for i in range(0, len(vents_alt_row)-1,2):
                formatted_vent[counter].append([int(vents_alt_row[i]),int(vents_alt_row[i+1])])

    return nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, formatted_vent