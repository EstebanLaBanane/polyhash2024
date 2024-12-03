def read(fichier) :
    """
    :param  :   fichier : .in
    :return :   RowMap :        int
                ColMap :        int
                AltMap :        int
                NbTargetCells : int
                CoverageRadius: int
                NbBalloons :    int
                NbTurns :       int
                StartingCell :  list[int]
                TargetCells :   list[list[int]]
                WindDirectory : list[list[list[list[int]]]]
    """
    with open(fichier, 'r') as input:
        data = input.readline().split(" ")
        (RowMap,ColMap,AltMap) = (int(data[0]),int(data[1]),int(data[2]))

        data = input.readline().split(" ")
        (NbTargetCells,CoverageRadius,NbBalloons,NbTurns) = (int(data[0]),int(data[1]),int(data[2]),int(data[3]))

        data = input.readline().split(" ")
        StartingCell = [int(data[0]),int(data[1])]

        TargetCells = []
        for i in range(NbTargetCells) :
            data = input.readline().split(" ")
            TargetCells.append([int(data[0]),int(data[1])])

        WindDirectory = [[[[] for a in range(AltMap)]for c in range(ColMap)] for r in range(RowMap)]
        for a in range(AltMap) :
            for r in range(RowMap) :
                data = [int(s) for s in (input.readline()).split(" ")]
                for c in range(ColMap) :
                    WindDirectory[r][c][a] = [data[c*2],data[c*2+1]]

        input.close()
        return RowMap,ColMap,AltMap,NbTargetCells,CoverageRadius,NbBalloons,NbTurns,StartingCell,TargetCells,WindDirectory


"""
(r,c,a,nbt,cov,nbb,turns,start,target,wind) = read('a_example.in')
print(r,c,a,nbt,cov,nbb,turns,start,target)
for j in range(r):
    for k in range(c):
        print(wind[j][k][0],wind[j][k][1],wind[j][k][2])
    print("\n")
"""
