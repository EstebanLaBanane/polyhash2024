from game import Game

def get_instructions(g : Game, algo : callable)-> list[list[int]]:
    return algo(g)