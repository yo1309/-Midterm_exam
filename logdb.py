import sqlite3

def dbcon():
    return sqlite3.connect('join.db')

def create_table(): 
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE users (id varchar(50), pw varchar(50), name varchar(30))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(id, pw, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw, name)
        c.execute("INSERT INTO users VALUES(?,?,?)", setdata)
        db.commit()
    except Exception as e:
        print('db error', e)
    finally:
        db.close()
    
def select_all(): 
    ret = list() 
    try: 
        db = dbcon() 
        c = db.cursor() 
        c.execute('SELECT * FROM users') 
        ret = c.fetchall() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
        return ret

def select_users(id,pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute('SELECT * FROM users WHERE id=? and pw=?',setdata)
        ret =c.fetchone()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()
        return ret

#create_table()









