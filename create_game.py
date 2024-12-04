from read_input import read
from game       import Game
from map        import Map
from balloon    import Balloon
from gui        import create_canvas


def create_game(file_path, DEBUG_MODE) -> Game:
    nb_row, nb_col, nb_alt, nb_tgt_cell, cov_r, nb_balloon, turns, start_row, start_col, targets_pos, vents_alt = read(file_path)
    game_map = Map(start_row,start_col,nb_row,nb_col,nb_alt,vents_alt,targets_pos)

    balloons = []
    start_cell = game_map.get_cell(start_row, start_col)
    for i in range(nb_balloon):
        new_balloon = Balloon(start_cell,0,cov_r,i)
        balloons.append(new_balloon)
        start_cell.is_covered = True

    canvas = None

    if DEBUG_MODE:
        canvas = create_canvas()    
    
    game = Game(balloons,game_map,turns,canvas)
    return game