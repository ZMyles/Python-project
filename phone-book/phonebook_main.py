


from tkinter import *
import tkinter as tk


# Be sure to import our other modules 
# so we can have access to them
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame ================

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300) #(HIGHT/ WIDTH)
        self.master.maxsize(500,300)

        phonebook_func.center_window(self,500,300)
        self.master.configure(bg= "#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master


        phonebook_gui.load_gui(self)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
