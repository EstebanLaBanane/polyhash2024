from tkinter    import *
from game       import Game

def create_canvas():
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()-50
    canva = Canvas(root,width=w,height=h,background='skyblue')

    return canva

def show_game(g : Game):
    g.canva.delete("all")
    root1 = Tk()
    w, h = root1.winfo_screenwidth(), root1.winfo_screenheight() - 50
    root1.destroy()
    nb_col  = g.game_map.cols
    lar_col = (w-50) / nb_col

    nb_row  = g.game_map.rows
    lar_row = (h-50) / nb_row

# Creation grille verticale
    for i in range(0,nb_col+1):
        l = g.canva.create_line(i*lar_col+25,25,i*lar_col+25,h-25)

# Creation grille horizontale
    for i in range(0,nb_row+1):
        l = g.canva.create_line(25,i*lar_row+25,w-25,i*lar_row+25)

# Affichage des targets
    for t in g.game_map.get_targets():
        col = t.col
        row = t.row

        c_pos = col*lar_col+25
        r_pos = row*lar_row+25

        if t.is_covered:
            g.canva.create_rectangle(c_pos,r_pos,c_pos+lar_col,r_pos+lar_row,fill='green')
        else:
            g.canva.create_rectangle(c_pos,r_pos,c_pos+lar_col,r_pos+lar_row,fill='white')

        
# Affichage de la position du lancement
    start_col = g.game_map.start_col
    start_row = g.game_map.start_row
    start_c_pos = start_col*lar_col+25
    start_r_pos = start_row*lar_row+25
    g.canva.create_rectangle(start_c_pos,start_r_pos,start_c_pos+lar_col,start_r_pos+lar_row,fill='purple')
    g.canva.create_text(start_c_pos+lar_col/2,start_r_pos+lar_row/2,text="Start",font=('Helvetica {}'.format(str(int(lar_col/4)))))

# Affichage des ballons
    counter = 1
    for b in g.balloons:
        col = b.cell.col
        row = b.cell.row

        if col !=-1 and row != -1:
            c_pos = col*lar_col+25
            r_pos = row*lar_row+25
            if b.altitude > 0:
                g.canva.create_oval(c_pos,r_pos,c_pos+lar_col,r_pos+lar_row,outline='red',fill='red')
                g.canva.create_text(c_pos+lar_col/2,r_pos+lar_row/2,text=str(counter),font=('Helvetica {}'.format(str(int(lar_col/2)))))
            else:
                g.canva.create_oval(c_pos,r_pos,c_pos+lar_col,r_pos+lar_row,outline='red')
        counter +=1

    g.canva.pack()
    g.canva.update()
    # root.mainloop()