
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def data_entry():
    for filename in fileList:
        if filename.endswith(".txt"):
            cur.execute("INSERT INTO tbl_fileList(col_file) VALUES(?)", (filename,))
            print(filename)
    conn.commit()

data_entry()





conn.close()
    
        


