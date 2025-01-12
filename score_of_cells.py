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

    #RIEN NE MARCHE AAAAAAAAAAAAAAAAA

    #on fait pour chaque cell une liste de toutes les cases touchées (en imaginant que il y'a un balloon dessus) et pour chaque target_id qui se trouve dans cette liste on ajoute 1 a cell_score
    def calculate_list_cov_cells(id_cell,cell_col,cell_row,list_cov_cells:list):
#il y'a un probleme ici dans la maniere avec laquelle j'append list_cov_cells
        list_cov_cells.append(id_cell)
        for row in range (nb_row):
            for col in range(nb_col):
                cell_to_cov_id=row*nb_col+col
                if (cell_row-row)**2+min(abs(cell_col-col),nb_col-(abs(cell_col-col)))**2<=nb_row**2 and row*nb_col+col not in list_cov_cells:
                    list_cov_cells.append(row*nb_col+col)
        return list_cov_cells

    return calculate_list_cov_cells(7,2,1,[])








print(score_of_cells("challenges/a_example.in"))


        """"if cov_r==-1:
            #return list_cov_cells

        if id_cell not in list_cov_cells:
            #list_cov_cells.append(id_cell)

        for i in range(0,cov_r+1):
            print(id_cell+(i*nb_col),id_cell-(i*nb_col),len(formatted_vent[0]) )
            if id_cell+(i*nb_col)<len(formatted_vent[0]) and id_cell+ (i*nb_col) not in list_cov_cells:
                list_cov_cells.append(id_cell+ (i*nb_col))
            if id_cell-(i*nb_col)>=0 and id_cell- (i*nb_col) not in list_cov_cells:
                list_cov_cells.append(id_cell- (i*nb_col))
        #ATTENTION il faut prendre en compte le fait que a droite ca repasse a gauche C EST PAS ENCORE IMPLEMENTE




        if id_cell+1<nb_row*(id_cell//nb_row +1):
            for i in range (len(calculate_list_cov_cells(id_cell+1,cov_r-1,list_cov_cells))):
                if calculate_list_cov_cells(id_cell+1,cov_r-1,list_cov_cells)[i] not in list_cov_cells:
                    list_cov_cells.append(calculate_list_cov_cells(id_cell+1,cov_r-1,list_cov_cells)[i])




        return list_cov_cells

    return calculate_list_cov_cells(7,cov_r, [])
        #right_path=calculate_list_cov_cells(id_cell+1,cov_rad-1)
        #left_path=calculate_list_cov_cells(id_cell-1,cov_rad-1)





#il faut imaginer que chaque cell est un ballon et calculer le nombre de targets qu'elle touche ou calculer la distance depuis la cell vers toutes les targets.
#si la distance est inferieur a la distance maximal pour toucher (qui est en fonction du cov_r) alors elle marque un point.
print(score_of_cells("challenges/a_example.in"))"""