from read_input import read


def cut_map_optimise(file_path):
    #recuperation des données
    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, vents_alt = read(file_path)
    #calcul de la zone effectif
    zone_eff=(2*cov_r+1)**2
    row_eff=(zone_eff)**(1/2)
    col_eff=(zone_eff)**(1/2)

    #cette fonction decoupe un bloque en fct de la zone effectif
    def cut_bloc(indice_row:int,indice_col:int,row_eff,col_eff):
        bloc=[]
        for row in range(int(row_eff)):
            for col in range(int(col_eff)):
                bloc.append([row+indice_row,col+indice_col])
        return bloc


    def Map_bloc(map,nb_row,nb_col,row_eff,col_eff,reste_col:int=0,reste_row:int=0):
        row = 0
        col = 0
        for i in range((nb_row//int(row_eff))):
            #dans le cas ou on a n/row_effectif != int (il y a un reste)
            for j in range((nb_col // int(col_eff))):
                    # dans le cas ou on a n/col_effectif != int (il y a un reste) et n/row_effectif != int (il y a un reste)
                    if reste_col!=0 and reste_row!=0 and j==(nb_col//int(col_eff))-1 and i==(nb_row//int(row_eff))-1 :
                        bloc = cut_bloc(row, col, row_eff+reste_row, col_eff+reste_col)
                        map.append(bloc)
                        col += int(col_eff)
                    #dans le cas ou on a n/col_effectif != int (il y a un reste) et n/row_effectif = int (il y a pas de reste)
                    elif reste_col != 0 and j == (nb_col // int(col_eff)) - 1:
                        bloc = cut_bloc(row, col, row_eff, col_eff + reste_col)
                        map.append(bloc)
                        col += int(col_eff)

                    # dans le cas ou on a n/col_effectif = int (il y a pas de reste) et n/row_effectif != int (il y a un reste)
                    elif reste_row!=0 and i==(nb_row//int(row_eff))-1:
                        bloc = cut_bloc(row, col, row_eff+reste_row, col_eff)
                        map.append(bloc)
                        col += int(col_eff)

                    #sinon dans le cas normal
                    else:
                        bloc = cut_bloc(row, col, row_eff, col_eff)
                        map.append(bloc)
                        col += int(col_eff)

            col=0
            row += int(row_eff)
        return map

    map=[]
    reste_row = int(nb_row % int(row_eff))
    reste_col = int(nb_col % int(col_eff))
    return Map_bloc(map,nb_row,nb_col,row_eff,col_eff,reste_col,reste_row)

def display(blocks, blocks_per_row):
    # Trouver la hauteur et la largeur maximales pour un bloc
    block_height = max(cell[0] for block in blocks for cell in block) + 1
    block_width = max(cell[1] for block in blocks for cell in block) + 1

    # Convertir chaque bloc en une grille avec ses coordonnées
    block_grids = []
    for block in blocks:
        # Calculer les dimensions locales du bloc
        min_x = min(cell[0] for cell in block)
        min_y = min(cell[1] for cell in block)
        max_x = max(cell[0] for cell in block)
        max_y = max(cell[1] for cell in block)

        height = max_x - min_x + 1
        width = max_y - min_y + 1

        # Créer une grille vide
        grid = [["     " for _ in range(width)] for _ in range(height)]
        for cell in block:
            x, y = cell
            grid[x - min_x][y - min_y] = f"{x},{y}"

        # Ajouter le bloc converti
        block_grids.append(grid)

    # Organiser les blocs en une carte
    map_rows = []
    for i in range(0, len(blocks), blocks_per_row):
        row_blocks = block_grids[i:i + blocks_per_row]

        # Trouver la hauteur maximale de la ligne actuelle
        max_block_height = max(len(block) for block in row_blocks)

        # Construire les lignes de la carte
        for line_index in range(max_block_height):
            row = []
            for block in row_blocks:
                if line_index < len(block):
                    row.append("  ".join(block[line_index]))
                else:
                    row.append(" " * (len(block[0]) * 6))  # Espaces pour blocs courts
            map_rows.append("     ".join(row))  # Séparateur entre blocs

        # Ajouter une ligne vide pour espacer les rangées de blocs
        map_rows.append("")

    # Retourner la chaîne combinée
    return "\n".join(map_rows)

