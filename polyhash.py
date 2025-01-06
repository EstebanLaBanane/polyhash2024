import sys
from create_game        import create_game
from game               import Game
from get_instructions import get_instructions
from algos.rando_algo   import rando_algo
from gui                import show_game
import time
from algos.Main_Algo import Main_Algo

from balloon import Balloon
from algos.Decoupe_OPT import cut_map_optimise
from algos.Diriger_Ballon import assignation_ballon_vers_zones
from algos.ZonePoints import concentration_cells_pts
from algos.find_dead_cells import find_dead_cells


def main()-> None:
    source = sys.argv[1]
    destination = sys.argv[2]
    destination_f = open(destination,'w')

    DEBUG_MODE = True

    game = create_game(source,DEBUG_MODE)

    #algorithm = rando_algo
    algorithm = Main_Algo

    while game.turns > 0:
        MapBloc = cut_map_optimise(source)
        ZonesPts = concentration_cells_pts(source)
        nb_balloon = len(game.balloons)
        dictBallonZone = assignation_ballon_vers_zones(nb_balloon, ZonesPts)
        deadcells=find_dead_cells(source)
        instruction = get_instructions(game,algorithm,MapBloc,dictBallonZone,deadcells)
        #instruction = get_instructions(game,algorithm)
        game.update(instruction)
        instruction_str = ""
        for balloon_cmd in instruction:
            instruction_str += str(balloon_cmd) + " "
        instruction_str =instruction_str[:-1] + "\n"
        destination_f.write(instruction_str)
        
        if any([b.is_alive for b in game.balloons]):
             show_game(game)
             time.sleep(2)

    destination_f.close()
    print("Score final : {}".format(str(game.score)))

main()