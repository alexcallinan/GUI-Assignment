from tkinter import *
import random
import time

class ClickClick:
    def __init__(self,master):
        self.master = master
        self.create()

    counter=0

    def score(self):
        ClickClick.counter+=1
        self.lab['text'] = ('Score:', ClickClick.counter)

    def create(self):
        self.f = Frame(self.master, bg='green', height=550, width=500)
        self.f.pack()
        self.c= Canvas(self.f,bg='light green',height=500,width=500,highlightthickness=0)
        self.c.pack(side=BOTTOM)
        self.lab= Label(self.f,text=('Score:',0),fg='White',bg='green',font='Calibri 16 bold')
        self.lab.pack(side=RIGHT)
        self.but=Button(self.f,text='Start Game',command=self.start,bg='green',fg='white',font='Calibri 10 bold')
        self.but.pack(side=LEFT)

    def start(self):
        self.c.delete('all')
        xpos = random.randint(1, 450)
        ypos = random.randint(1, 450)
        self.milsec2 = int(round(time.time() * 1000))
        self.oval=self.c.create_oval(xpos,ypos,xpos+20,ypos+20,fill='grey')
        self.c.tag_bind(self.oval,'<Button-1>',self.oval_click)

    def oval_click(self,event):
        self.milsec1 = int(round(time.time() * 1000))
        if (self.milsec1-self.milsec2)<=2000:
            self.score()
        self.milsec3 = int(round(time.time() * 1000))
        xpos = random.randint(1, 450)
        ypos = random.randint(1, 450)
        self.c.delete('all')
        self.oval2 =self.c.create_oval(xpos,ypos,xpos+20,ypos+20,fill='grey')
        self.c.tag_bind(self.oval2,'<Button-1>',self.oval2_click)

    def oval2_click(self,event):
        self.milsec = int(round(time.time() * 1000))
        if (self.milsec-self.milsec3)<=2000:
            self.score()
        xpos = random.randint(1, 450)
        ypos = random.randint(1, 450)
        self.milsec2 = int(round(time.time() * 1000))
        self.c.delete('all')
        self.oval3=self.c.create_oval(xpos,ypos,xpos+20,ypos+20,fill='grey')
        self.c.tag_bind(self.oval3,'<Button-1>',self.oval_click)


if __name__ == '__main__':
    root = Tk()
    app = ClickClick(root)
    root.mainloop()


