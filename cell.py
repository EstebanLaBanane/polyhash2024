class Cell:
    id          : int
    row         : int
    col         : int
    winds       : list[list[int]]
    is_target   : bool
    is_covered  : bool

    def __init__(self, id, row, col, winds, is_target, is_covered = False):
        self.id         = id
        self.row        = row
        self.col        = col
        self.winds      = winds
        self.is_target  = is_target
        self.is_covered = is_covered

    def __str__(self):
        return "c" + str(self.id) + " : " + str(self.row) + ", " + str(self.col)

    def __repr__(self):
        return "c" + str(self.id) + " : " + str(self.row) + ", " + str(self.col)
    
    
    def get_wind(self, altitude : int):
        print(self, self.winds)
        return self.winds[altitude-1]