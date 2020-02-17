import _tkinter
import tkinter as tk
import random
from functions import *
# Use Tkinter for python 2, tkinter for python 3
data = get_data()

diff_list = diff_data(data, 3)

class a_drop:
    def __init__(self,width, height, color = None):
        self.x=random.randint(0,width)
        self.y=random.randint(0,height)
        self.cv = None
        self.r=0
        self.a=random.randint(1,5)*1.
        self.v = 1
        if color == "red":
            self.color='#%02x%02x%02x' % (255,0,0)
        elif color == "green":
            self.color='#%02x%02x%02x' % (0,255,0)
        else:
            self.color='#%02x%02x%02x' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.drops = []
        self.canvas = tk.Canvas(parent, height = 728, width = 1288,bg= 'black')
        self.canvas.pack()

        self.window_init()
        self.count = 0
    def window_init(self):

        self.parent.title("Raindrops of the World")
        
    def update_drops(self, ):
        if diff_list[self.count] > 0:
            self.drops.append(a_drop(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), color = 'green'))
        else:    
            self.drops.append(a_drop(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), color = 'red'))
        
        self.count += 1
        toremove=[]
        for idx, drop_ in enumerate(self.drops):
            self.drops[idx].r += self.drops[idx].v
            self.drops[idx].a -= 0.05
            if self.drops[idx].a  <= 0.:
                toremove.append(idx)
            else:
                if self.drops[idx].cv:
                    self.canvas.delete(self.drops[idx].cv)
                self.drops[idx].cv = self.canvas.create_oval(self.drops[idx].x-self.drops[idx].r, self.drops[idx].y-self.drops[idx].r, self.drops[idx].x+self.drops[idx].r, self.drops[idx].y+self.drops[idx].r)
                self.canvas.itemconfig(self.drops[idx].cv, outline=self.drops[idx].color)
                self.canvas.itemconfig(self.drops[idx].cv, width=self.drops[idx].a)
        for i in toremove:
            self.canvas.delete(self.drops[i].cv)
            self.drops.pop(i)
        self.canvas.update()

#. By doing the main check, you can have that code only execute 
# when you want to run the module as a program,
#  and not have it execute when someone just wants to import your module,
#  and call your functions themselves
if __name__ == "__main__":
    root = tk.Tk()
    main = MainApplication(root)
    #root.geometry("400x400")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    
    for i in range(len(diff_list)):
        main.update_drops()
        main.after(1)
