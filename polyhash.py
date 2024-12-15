import sys
from create_game        import create_game
from game               import Game
from get_instructions   import get_instructions
from algos.rando_algo   import rando_algo
from gui                import show_game
import time


from balloon import Balloon

def main()-> None:
    source = sys.argv[1]
    destination = sys.argv[2]
    destination_f = open(destination,'w')

    DEBUG_MODE = True

    game = create_game(source,DEBUG_MODE)

    algorithm = rando_algo

    while game.turns > 0:
        instruction = get_instructions(game,algorithm)

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