import sqlite3 as sq

def task_list_create():
    try:
        con = sq.connect('task_list.db')
        cursor = con.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS task(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           task_name TEXT NOT NULL,
                           des TEXT,
                           completed NUMBER NOT NULL DEFAULT 0 
                       )
            ''')
        '''
        0 = not in progress
        1  = in progress
        2 = done
        '''
    except sq.Error as e:
        print(f"ERROR , TIPO DE ERROR: {e}")
    finally:
        if con:
            con.commit()
            con.close()
            

    
    
        
        