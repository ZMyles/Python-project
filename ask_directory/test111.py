import tkinter.filedialog
from tkinter import *




class UserInferFace(Frame):
    def __init__ (self,master):
        Frame.__init__(self)



#Layout ================================
        self.master = master
        self.master.resizable(width =True, height=True)
        self.master.title('Find Directory')
        self.master.geometry('{}x{}'.format(700,300))

        #Buttons============================================
        self.Search = Button(self.master, text = 'Browse', width=15, height= 2, command=self.openDir)
        self.Search.grid(row=2, column=1, padx=(30,0), pady=(30, 0))

        #Text Box==========================================
        self.txtWidget = Text(self.master, width=80, height= 2)
        self.txtWidget.grid(row=3, column=1, padx=(30,0), pady=(30,0))


#Function ============================
    def openDir(self):
        tn = filedialog.askdirectory()
        self.txtWidget.insert(INSERT, tn)
        print(tn)
          
if __name__ == "__main__":
    root = Tk()
    App = UserInferFace(root)
    root.mainloop()



