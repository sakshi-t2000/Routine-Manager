import sqlite3

def connect():
    conn= sqlite3.connect('routine.db')
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY, date text, earning integer, exercise text, study text, moneyspent integer, python text)")
    conn.commit()
    conn.close()
        
    
def insert(date, earning, exercise, study, moneyspent, python):
    conn= sqlite3.connect('routine.db')
    cur= conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL,?,?,?,?,?,?)",(date, earning, exercise, study, moneyspent, python))
    conn.commit()
    conn.close() 

def view():
    conn= sqlite3.connect('routine.db')
    cur= conn.cursor()
    cur.execute("SELECT *FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close() 
    return rows

def delete(id):
    conn= sqlite3.connect('routine.db')
    cur= conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?" ,(id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close() 
    return rows

def search(date='', earning='', exercise='', study='', moneyspent='', python=''):
    conn= sqlite3.connect('routine.db')
    cur= conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earning=? OR exercise=? OR study=? OR moneyspent=? OR python=?",(date, earning, exercise, study, moneyspent, python))
    rows = cur.fetchall()
    conn.commit()
    conn.close() 
    return rows

#insert('22-1-2000',1000,'no exercise','no study',10,'yes')

connect()



    

    

















#print(view())
    






