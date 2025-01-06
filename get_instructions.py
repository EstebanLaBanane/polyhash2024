from game import Game

#def get_instructions(g : Game, algo : callable)-> list[list[int]]:
#   return algo(g)

def get_instructions(g:Game,algo:callable,MapBloc,dictBallonZone,deadcells)->list[list[int]]:
    return algo(g,MapBloc,dictBallonZone,deadcells)