import os
import tkinter.filedialog
from tkinter import *


class UserFace(Frame):
    def __init__(self,master):
        Frame.__init__(self)

#Layout======================================
        self.master = master
        self.master.title('Folder Finder')
        self.master.geometry('{}x{}'.format(700,400))

        #Buttons=====================================
        self.Search = Button(self.master, command=self.sourceFile, text = "Browse files", width=15, height=2)
        self.Search.grid(row=2, column=1, padx=(30,0), pady=(30,0))

        self.Search = Button(self.master, command=self.destinationPath, text = "PLACE HOLDER", width=15, height=2)
        self.Search.grid(row=3, column=1, padx=(30,0), pady=(40,0))

        #Output Text=================================
        self.outPut1 = Text(self.master, width= 40, height=2)
        self.outPut1.grid(row=3, column=5, padx=(30,0), pady=(30,0))

        self.outPut2 = Text(self.master, width= 40, height=2)
        self.outPut2.grid(row=3, column=5, padx=(30,0), pady=(100,0))

#Function====================================
    def sourceFile(self):
        fileP = filedialog.askdirectory()
        self.outPut1.insert(INSERT, fileP)
        print(fileP)


    def destinationPath(self):
        fileP2 = filedialog.askdirectory()
        self.outPut2.insert(INSERT, fileP2)
        print(fileP2)
        

if __name__=="__main__":
    root = Tk()
    App = UserFace(root)
    root.mainloop()
