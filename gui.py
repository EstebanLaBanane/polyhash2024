from tkinter    import *
from game       import Game

def show_game(g : Game):
    root = Tk()

    canva = Canvas(root,width=1900,height=1025,background='skyblue')

    nb_col  = g.game_map.cols
    lar_col = 1850 / nb_col

    nb_row  = g.game_map.rows
    lar_row = 975 / nb_row

# Creation grille verticale
    for i in range(0,nb_col+1):
        l = canva.create_line(i*lar_col+25,25,i*lar_col+25,1000)

# Creation grille horizontale
    for i in range(0,nb_row+1):
        l = canva.create_line(25,i*lar_row+25,1875,i*lar_row+25)

# Affichage des targets
    for t in g.game_map.get_targets():
        col = t.col
        row = t.row

        c_pos = col*lar_col+25
        r_pos = row*lar_row+25

        canva.create_rectangle(c_pos,r_pos,c_pos+lar_col,r_pos+lar_row,fill='green')

# Affichage de la position du lancement
    start_col = g.game_map.start_col
    start_row = g.game_map.start_row
    start_c_pos = start_col*lar_col+25
    start_r_pos = start_row*lar_row+25
    canva.create_rectangle(start_c_pos,start_r_pos,start_c_pos+lar_col,start_r_pos+lar_row,fill='purple')
    canva.create_text(start_c_pos+lar_col/2,start_r_pos+lar_row/2,text="Start",font=('Helvetica {}'.format(str(int(lar_col/4)))))

# Affichage des ballons
    counter = 1
    for b in g.balloons:
        col = b.cell.col
        row = b.cell.row

        if col !=-1 and row != -1:
            c_pos = col*lar_col+25
            r_pos = row*lar_row+25
            if b.altitude > 0:
                canva.create_oval(c_pos,r_pos,c_pos+lar_col,r_pos+lar_row,outline='red',fill='red')
                canva.create_text(c_pos+lar_col/2,r_pos+lar_row/2,text=str(counter),font=('Helvetica {}'.format(str(int(lar_col/2)))))
            else:
                canva.create_oval(c_pos,r_pos,c_pos+lar_col,r_pos+lar_row,outline='red')
        counter +=1

    canva.pack()
    root.mainloop()