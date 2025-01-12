from read_input import read


def score_of_cells(filepath):
    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, formatted_vent = read(filepath)
    score_map={}
    list_id_targets=[]


    #on fait la liste des id des targets
    for target in targets_pos:
        tg_row=target[0]
        tg_col=target[1]

        cell_id=tg_row*nb_col+tg_col
        list_id_targets.append(cell_id)




    #on fait une fonction qui en prenant une cell elle donne une liste de toutes les cases touchées (en imaginant que il y'a un balloon dessus)

    def calculate_list_cov_cells(id_cell,cell_col,cell_row,list_cov_cells:list):
        list_cov_cells.append(id_cell)
        for row in range (nb_row):
            for col in range(nb_col):
                cell_to_cov_id=row*nb_col+col
                if (cell_row-row)**2+min(abs(cell_col-col),nb_col-(abs(cell_col-col)))**2<=cov_r**2 and row*nb_col+col not in list_cov_cells:
                    list_cov_cells.append(row*nb_col+col)
        return list_cov_cells



    #on crée le dict cell_scores qui aura comme clé l'indice d'une cellule et comme valeur son score

    cell_scores={}
    map=[]
    for row in range(nb_row):
        for col in range(nb_col):
            map.append([row,col])
    for i in range(len(map)):
        cell_cords=map[i]
        cell_row=cell_cords[0]
        cell_col=cell_cords[1]
        id=nb_col*cell_row + cell_col
        if id not in cell_scores:
            cell_scores[id]=0
        list_cov_cells=calculate_list_cov_cells(id,cell_col,cell_row,[])
        for target in list_id_targets:
            if target in list_cov_cells:
                cell_scores[id]+=1

    return cell_scores



#idée: il faut trouver des patterns de suite de chiffres >0 de suite. exemple : "1 3 4 5 54 8 9"








