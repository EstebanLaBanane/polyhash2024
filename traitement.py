def MapReading(fichier:str):
    f=open(fichier,'r')
    firstline=f.readline()
    L=firstline.split()
    for i in range(len(L)):
        L[i]=int(L[i])
    RowMap=L[0]
    ColMap=L[1]
    AltMap=L[2]
    f.close()
    return RowMap,ColMap,AltMap

def GameInfo(fichier:str):
    f=open(fichier,'r')
    n=2
    line=0
    for j in range(n):
        line=f.readline()
    L=line.split()
    for i in range(len(L)):
        L[i]=int(L[i])
    NbTargetCells=L[0]
    CoverageRadius=L[1]
    NbBalloons=L[2]
    NbTurns=L[3]
    f.close()
    return NbTargetCells,CoverageRadius,NbBalloons,NbTurns

def StartingCellReading(fichier:str):
    f = open(fichier, 'r')
    n = 3
    line = 0
    for j in range(n):
        line = f.readline()
    L = line.split()
    for i in range(len(L)):
        L[i] = int(L[i])
    RowStartingCell = L[0]
    ColStartingCell = L[1]
    return RowStartingCell,ColStartingCell

def TargetCellPositions(fichier:str,NbTargetCells:int):
    f = open(fichier, 'r')
    n = 3+NbTargetCells
    line = ""
    for j in range(n):
        if j<=2:
           f.readline()
        else:
            line+=f.readline()

    L = line.split()
    for i in range(len(L)):
        L[i] = int(L[i])
    for k in range(len(L)):
        if k%2==0:
            RowTargetCell=L[k]
            ColTargetCell=L[k + 1]
            yield RowTargetCell,ColTargetCell
    f.close()

def WindReading(fichier:str,NbTargetCells:int,RowMap:int,ColMap:int,AltMap:int):
    f = open(fichier, 'r')
    n = 3 + NbTargetCells
    line = ""
    for j in range(n+RowMap*AltMap):
        if j <= n:
            f.readline()
        else:
            line += f.readline()
    L = line.split()
    for i in range(len(L)):
        L[i] = int(L[i])
    for z in range(len(L)):
        M=[]




    """for k in range(len(L)):
        if k % 2 == 0:
            RowTargetCell = L[k]
            ColTargetCell = L[k + 1]
            yield RowTargetCell, ColTargetCell"""
    f.close()



def main():
    nom="challenges/a_example.in"
    print(WindReading(nom,2,3,5,3))

if __name__ == "__main__":
    main()