import os
import time

"""
def writeData():
    data = "Hello World!"
    with open('Red dragon.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('Red dragon.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()



if __name__ == "__main__":
##   writeData()
    openFile()
"""

##===============


files = os.listdir("..\Python-Drill")


now = os.getcwd()

for file in files:
   ## print(os.path.join(now, file))    
    modification_time = os.path.getmtime(file)

local_time = time.ctime(modification_time)
print("Last modification time(local time: {})".format(local_time))


    






