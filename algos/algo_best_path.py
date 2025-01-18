from game       import Game
from collections.abc import Callable, Iterable , Iterator


def path_max_rec(g : Game , instruction) -> (int,list[int]):
    inst = [instruction[-1]]
    g.update(inst)

    if g.turns == 0 or not g.balloons[0].is_alive :
        return (g.score,instruction)

    else :
        if g.balloons[0].altitude == g.game_map.nb_altitudes :
            (s1,i1) = path_max_rec(g,instruction+[0])
            (s2,i2) = path_max_rec(g,instruction+[1])
            if s1 > s2 : return (s1,i1)
            else : return (s2,i2)

        elif g.balloons[0].altitude == 1 :
            (s1,i1) = path_max_rec(g,instruction+[0])
            (s2,i2) = path_max_rec(g,instruction+[1])
            if s1 > s2 : return (s1,i1)
            else : return (s2,i2)

        else :
            (s1,i1) = path_max_rec(g,instruction+[0])
            (s2, i2) = path_max_rec(g, instruction+[1])
            (s3, i3) = path_max_rec(g, instruction+[-1])
            if s1 > s2 and s1 > s3 : return (s1,i1)
            elif s2 > s1 and s2 > s3 : return (s2,i2)
            else : return (s3,i3)


def best_path(g : Game) -> list[int] :
    instruction = [1]
    g.balloons = g.balloons[:1]
    (s,instr) = path_max_rec(g,instruction)
    while len(instr) != g.max_turn :
        instr.append(0)
    return instr

'''
def produce_instruction(path : list[int],g : Game) -> list[int] :
    #appel à chaque tour pour avoir les instructions
    ln = len(path)
    b = len(g.balloons)
    instructions = [0 for i in range(ln)]
    instr = best_path(g)
    for i in range(max(current_turn,ln)) :
        for j in range(i) :
            instructions[i] = instr[current_turn-i]
    return instructions
'''

def produce_instruction_aux(path : list[int],g : Game) -> Iterator[list[int]] :
    #len(instr) == g.max_turns
    lnb = len(g.balloons)
    instru = [0 for i in range(lnb)]
    for i in range(g.max_turn) :
        for j in range(min(lnb,i)) :
            instru[j] = path[i-j]
        yield instru

def produce_instruction(path : list[int],g : Game) -> list[list[int]]:
    instr = []
    for i in produce_instruction_aux(path,g) :
        instr.append(i)
    return instr


