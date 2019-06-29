import os, sys
import tkinter.filedialog
from tkinter import *



files = os.listdir("../Final-Drill/Temp-Dir")#Path to the files in my Machine



class UserFace(Frame):
    def __init__(self,master):
        Frame.__init__(self)

#Layout/Display ======================================
        self.master = master
        self.master.title('Folder Finder')
        self.master.geometry('{}x{}'.format(700,400))

        #Buttons=====================================
        self.Search = Button(self.master, command=self.sourceFile, text = "Source Files", width=15, height=2)
        self.Search.grid(row=2, column=1, padx=(30,0), pady=(30,0))

        self.Search = Button(self.master, command=self.destinationPath, text = "Directory Path", width=15, height=2)
        self.Search.grid(row=3, column=1, padx=(30,0), pady=(40,0))

        
        self.Search = Button(self.master, command=self.swapDir, text = "PLACE HOLDER", width=15, height=2)
        self.Search.grid(row=4, column=1, padx=(30,0), pady=(40,0))

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
        

    def swapDir(self):
        for data in files:
            suffix = '.txt'
            textFile = data.endswith(suffix)
            if textFile == True:
                print(data)




"""
for file in files:
    print(os.path.join(file))
    path = "../Final-Drill/Temp-Dir"
"""




if __name__=="__main__":
    root = Tk()
    App = UserFace(root)
    root.mainloop()
