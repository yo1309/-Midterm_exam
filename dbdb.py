import sqlite3

def dbcon():
    return sqlite3.connect('mydb.db')

def create_table(): 
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE student (num varchar(50), name varchar(50)")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(num, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num, name)
        c.execute("INSERT INTO student VALUES(?,?)", setdata)
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
        c.execute('SELECT * FROM student') 
        ret = c.fetchall() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
        return ret

#create_table()
#insert_data('20201234','파이썬')
#insert_data('20201235','자바')
select_all()