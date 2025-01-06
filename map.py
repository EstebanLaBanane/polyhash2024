#from polyhash2024.cell import Cell
from cell import Cell
class Map:
    start_row   : int
    start_col   : int
    rows        : int
    cols        : int
    nb_altitudes   : int
    cells       : list[list[Cell]]

    def __init__(self,start_row : int, start_col : int, rows : int, cols : int, nb_altitudes : int, winds,target_pos):
        self.start_row      = start_row
        self.start_col      = start_col
        self.rows           = rows
        self.cols           = cols
        self.nb_altitudes   = nb_altitudes
        self.cells          = self.create_map(winds,target_pos)

    def __str__(self):
        return "Map de {} colonnes x {} lignes x {} altitudes".format(self.cols,self.rows,self.nb_altitudes)

    def create_map(self,winds, targets_pos):
        cell_map = []
        for i in range(self.rows):
            cell_map.append([])
            for j in range(self.cols):
                cell_map[i].append([])

        #Liste de chaque cellule dans la même position sur differente altitude
        for i in range(0,self.rows*self.cols):
            row = i//self.cols
            col = i-row*self.cols
            cell_winds = []

            for wind_alt in winds:
                cell_winds.append(wind_alt[i])
            #si la position de la cellule coincide avec les coord du target, is_target = True
            is_target = False
            for target_pos in targets_pos:
                if row==target_pos[0] and col==target_pos[1]:
                    is_target = True
                    break

            new_cell = Cell(i,row,col,cell_winds,is_target)
            cell_map[row][col] = new_cell
        return cell_map

    #obtenir une cellule si elle est dehors deadcell sinon cell
    def get_cell(self, row : int,col : int) -> Cell:
        dead_cell = Cell(-1,-1,-1,None,False)
        if col >= self.cols or col < 0 or row >= self.rows or row < 0: return dead_cell
        return self.cells[row][col]
    #parcours de toutes les cellules pour renvoyer target
    def get_targets(self)-> list[Cell]:
        targets = []
        for cells_row in self.cells:
            cell : Cell
            for cell in cells_row:
                if cell.is_target:
                    targets.append(cell)
        return targets
