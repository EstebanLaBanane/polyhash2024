from read_input import read


def score_of_cells(filepath):
    # Lecture des données
    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, formatted_vent = read(filepath)

    # Convertir les cibles en un ensemble pour des recherches plus rapides
    targets_set = set(tg_row * nb_col + tg_col for tg_row, tg_col in targets_pos)

    # Pré-générer les offsets pour les cellules couvertes par un ballon
    def generate_coverage_offsets():
        offsets = []
        for dr in range(-cov_r, cov_r + 1):
            for dc in range(-cov_r, cov_r + 1):
                if dr**2 + min(dc % nb_col, nb_col - dc % nb_col)**2 <= cov_r**2:
                    offsets.append((dr, dc))
        return offsets

    coverage_offsets = generate_coverage_offsets()

    # Calcul des scores des cellules
    cell_scores = {}
    for row in range(nb_row):
        for col in range(nb_col):
            cell_id = row * nb_col + col
            if cell_id not in cell_scores:
                cell_scores[cell_id] = 0

            # Parcourir les cellules couvertes
            for dr, dc in coverage_offsets:
                # Calculer les coordonnées des cellules couvertes
                covered_row = row + dr
                covered_col = (col + dc) % nb_col  # Gestion des colonnes circulaires

                # Vérifier si la cellule couverte est une cible
                if 0 <= covered_row < nb_row:  # Vérifier les bornes
                    covered_id = covered_row * nb_col + covered_col
                    if covered_id in targets_set:
                        cell_scores[cell_id] += 1

    return cell_scores














