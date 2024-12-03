class Cell:
    id          : int
    row         : int
    col         : int
    winds       : list[list[int]]
    is_target   : bool
    is_covered  : bool

    def __init__(self,id, row, col, winds, is_target, is_covered = False):
        self.id         = id
        self.row        = row
        self.col        = col
        self.winds      = winds
        self.is_target  = is_target
        self.is_covered = is_covered


    def get_wind(self, altitude : int):
        return self.winds[altitude-1]


dead_cell = Cell(-1,-1,-1,None,False)