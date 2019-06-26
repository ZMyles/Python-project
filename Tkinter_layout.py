import tkinter
from tkinter import *


class WindowDisplay(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title('Check files')
        self.master.geometry('{}x{}'.format(700, 220))
        
# Buttons =========================================
        self.btnBrowse = Button(self.master, text='Browse...', width=15, height=1)
        self.btnBrowse.grid(row=2, column=1, padx=(30,0), pady=(30, 0))

        self.btnBrowse = Button(self.master, text='Browse...', width=15, height=1)
        self.btnBrowse.grid(row=2, column=1, padx=(30,0), pady=(100, 0))

        self.btnBrowse = Button(self.master, text='Check for files...', width=15, height=2)
        self.btnBrowse.grid(row=3, column=1, padx=(30,0), pady=(10, 0))
        

        self.btnBrowse = Button(self.master, text='Close program', width=15, height=2)
        self.btnBrowse.grid(row=3, column=4, padx=(400,0), pady=(10, 0))
        
# Inputs =========================================

        self.varBrowse_1 = StringVar()
        self.varBrowse_2 = StringVar()


        self.input1 = Entry(self.master, text=self.varBrowse_1, font=('Helvetica', 16), fg='black', bg='white', width=40)
        self.input1.grid(row=2, column=4, padx=(30, 0), pady=(40, 0))


        self.input1 = Entry(self.master, text=self.varBrowse_1, font=('Helvetica', 16), fg='black', bg='white', width=40)
        self.input1.grid(row=2, column=4, padx=(30, 0), pady=(100, 0))

        




if __name__ == "__main__":
    root = Tk()
    App = WindowDisplay(root)
    root.mainloop()
