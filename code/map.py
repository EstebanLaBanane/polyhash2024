from cell import Cell,dead_cell

class Map:
    start_row   : int
    start_col   : int
    rows        : int
    cols        : int
    nb_altitudes   : int
    cells       : list[list[Cell]]

    def __init__(self,start_row : int, start_col : int, rows : int, cols : int, nb_altitudes : int, winds : list[list[list[list[int]]]],target_pos : list[list[int]]):
        self.start_row      = start_row
        self.start_col      = start_col
        self.rows           = rows
        self.cols           = cols
        self.nb_altitudes   = nb_altitudes
        self.cells          = self.create_map(winds,target_pos)

    def __str__(self):
        return "Map de {} colonnes x {} lignes x {} altitudes".format(self.cols,self.rows,self.nb_altitudes)


    def create_map(self,winds : list[list[list[list[int]]]], targets_pos : list[list[int]]):
        cell_map = [[dead_cell for i in range(self.cols)] for j in range(self.rows)]

        for r in range(self.rows) :
            for c in range(self.cols) :
                new_cell = Cell(r*self.cols+c , r , c , winds[r][c] , False , False)
                cell_map[r][c] = new_cell

        def target(map,targets_pos) :
            #met true à is_target aux cells dont les coord sont dans targets_pos
            for targ in targets_pos :
                map[targ[0]][targ[1]].is_target = True

        target(cell_map,targets_pos)
        return cell_map


    def get_cell(self, row : int,col : int) -> Cell:
        if col >= self.cols or col < 0 or row >= self.rows or row < 0 :
            return dead_cell
        return self.cells[row][col]
    
    def get_targets(self) -> list[Cell]:
        targets = []

        for cells_row in self.cells:
            cell : Cell
            for cell in cells_row:
                if cell.is_target:
                    targets.append(cell)

        return targets