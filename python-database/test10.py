
import sqlite3

conn = sqlite3.connect('data-1.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS storage( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList TEXT)")
    conn.commit()
conn.close()
##=======================


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')



for data in fileList:
    suffix = '.txt'
    textFile = data.endswith(suffix)
    if textFile == True:
         print(data)


conn = sqlite3.connect('data-1.db')


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO storage(col_fileList) VALUES(?)", \
                ())

    conn.commit()
conn.close()   












    

