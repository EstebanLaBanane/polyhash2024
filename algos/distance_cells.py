
from math import *


def distance_cells(bal_cords,tar_cords):

    distance=sqrt(abs(bal_cords[0]-tar_cords[0])**2+abs(bal_cords[1]-tar_cords[1])**2)



    return distance

print(distance_cells([0,1],[0,3]))





