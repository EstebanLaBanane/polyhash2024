from read_input import read


def find_dead_cells(filepath):
    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, formatted_vent=read(filepath)
    health_cells={}
    #on parcourt toutes les altitudes
    for alt in range(nb_alt):
        tmp2=nb_row
        while tmp2 != 0:
            #on parcourt toutes les colonnes d'une ligne
            for i in range((nb_row - tmp2) * nb_col, (nb_row - tmp2) * nb_col + nb_col):

                #on regarde si la cellule est deja dans le dict.
                if i in health_cells.keys():

                    #si l'indicateur nord sud nous dis que cette cellule a une altitude donnée fais sortir le ballon de haut ou de bas alors ajoute "killer" a sa liste. Sinon ajoute "safe"
                    if nb_row-tmp2+formatted_vent[alt][i][0]<0 or nb_row-tmp2+formatted_vent[alt][i][0]>nb_row:
                            health_cells[i].append("killer")
                    else:
                            health_cells[i].append("safe")
                else:
                    if (nb_row-tmp2)+formatted_vent[alt][i][0]<0 or nb_row-tmp2+formatted_vent[alt][i][0]>nb_row:
                        health_cells[i]=["killer"]
                    else:
                        health_cells[i]=["safe"]

            tmp2-=1



    return health_cells


#print(find_dead_cells("../challenges/c_medium.in"))