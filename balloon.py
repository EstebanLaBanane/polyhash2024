from cell import Cell,dead_cell

class Balloon:
    cell                : Cell
    is_alive            : bool
    altitude            : int
    coverage_radius     : int
    balloon_id          : int

    def __init__(self, cell : Cell, altitude : int, coverage_radius :int,balloon_id : int):
        self.cell               = cell
        self.is_alive           = cell.col != -1 and cell.row != -1
        self.altitude           = altitude
        self.coverage_radius    = coverage_radius
        self.balloon_id         = balloon_id

    def __str__(self):
        return "Ballon {}, cellule : {}, altitude : {}, alive {}".format(self.balloon_id,self.cell,self.altitude,self.is_alive)

    def __repr__(self):
         return "Ballon {}, cellule : {}, altitude : {}, alive {}".format(self.balloon_id,self.cell,self.altitude, self.is_alive)

    # def death(self):
    #     self.cell = dead_cell
    #     self.is_alive = False
    #     self.altitude = 0