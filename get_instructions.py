from game import Game

#def get_instructions(g : Game, algo : callable,deadcells)-> list[list[int]]:
#   return algo(g,deadcells)

def get_instructions(g:Game,algo:callable,MapBloc,dictBallonZone,deadcells)->list[list[int]]:
    return algo(g,MapBloc,dictBallonZone,deadcells)