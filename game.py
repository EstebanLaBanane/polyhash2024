from balloon    import Balloon
from map        import Map
from cell       import Cell
from tkinter    import Canvas

class Game:
    balloons    : list[Balloon]
    game_map    : Map
    turns       : int   #number of turns until end
    max_turn    : int
    score       : int
    canva       : Canvas

    def __init__(self,balloons : list[Balloon], game_map : Map, turns : int,canva : Canvas | None = None):
        self.balloons   = balloons
        self.game_map   = game_map
        self.turns      = turns
        self.max_turn   = turns
        self.score      = 0
        self.canva      = canva
        

    # Bouge le ballon verticalement :
        # Si action impossible renvoie Exception
    def move_balloon_altitude(self,balloon_id : int, action : int):
        balloon = self.balloons[balloon_id]
        if not balloon.is_alive:
            return
        if action == 1:

            if balloon.altitude < self.game_map.nb_altitudes:
                balloon.altitude += 1
            else:
                raise Exception("Action impossible (Altitude maximum atteinte)")  
              
        elif action == -1:
            if balloon.altitude <= 1:
                raise Exception("Action impossible (On ne pas descendre un ballon au sol une fois lancé ou en dessous le sol)")
            
            balloon.altitude -= 1
                
    
    # Applique les vents a tout les ballons
    def apply_winds(self):
        for balloon in self.balloons:
            if balloon.is_alive and balloon.altitude != 0:
                wind_to_apply = balloon.cell.get_wind(balloon.altitude)
                current_cell_col = balloon.cell.col
                current_cell_row = balloon.cell.row
                new_row = current_cell_row + wind_to_apply[0]
                new_col = (current_cell_col + wind_to_apply[1]) % self.game_map.cols

                if new_row < 0 or new_row >= self.game_map.rows:
                    balloon.is_alive = False
                    dead_cell = Cell(-1,-1,-1,None,False)
                    balloon.cell = dead_cell
                else:
                    balloon.cell = self.game_map.get_cell(new_row,new_col)

    # Si target pas précisé, check toutes les targets
    def check_covers(self,balloon : Balloon,target : Cell) -> bool:
        if (balloon.cell.row == -1 and balloon.cell.col == -1):
            return False
        balloon_r   = balloon.cell.row
        balloon_c   = balloon.cell.col

        target_r    = target.row
        target_c    = target.col
        columndist  = min(abs(balloon_c - target_c),self.game_map.cols - abs(balloon_c - target_c))
        if (balloon_r - target_r)**2 + (columndist**2) <= balloon.coverage_radius**2:
            return True
        return False
    
    def check_coverage(self) -> None:
        for target in self.game_map.get_targets():
            target.is_covered = False
            for balloon in self.balloons:
                if self.check_covers(balloon,target):
                    target.is_covered = True

    def count_points(self) -> int:
        score = 0
        
        for target in self.game_map.get_targets():
            if target.is_covered:
                score += 1
        
        return score


    # Met a jour le jeu : 
        # S'il reste des turns (ie : self.turns > 0)
        # Parcours la liste d'action pour chaque ballon (1 -> monte, 0 -> reste, -1 -> descends)
        # ie. si actions = [1,0,-1,1] --> B0 monte, B1 reste, B2 descends, B3 monte
        # Apres les actions applique les mouvements du vent
        # Decremente turns a la fin
    def update(self, actions : list[int]) -> int | None:
        if self.turns==0:
            print("game ended")
            return self.score
        
        for i in range(0, len(actions)):
            self.move_balloon_altitude(i,actions[i])

        self.apply_winds()
        self.check_coverage()
        self.score += self.count_points()
        self.turns -= 1

        if self.turns==0:
            print("game ended")
            return self.score


