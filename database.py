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
        0 = not iun progress
        1  = in progress
        2 = done
        '''
    except sq.Error as e:
        print(f"ERROR , TIPO DE ERROR: {e}")
    finally:
        if con:
            con.commit()
            con.close()
            
def task_in_progress():
    try:
        conP = sq.connect('taskProgress.db')
        cursorP = conP.cursor()
        cursorP.execute('''
                        CREATE TABLE IF NOT EXISTS task_progress(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           task_name TEXT NOT NULL,
                           des TEXT,
                           completed NUMBER NOT NULL
                        ''')
    except sq.Error as e:
        print(f"ERROR , TIPO DE ERROR: {e}")
    finally:
        if conP:
            conP.commit()
            conP.close()
            
            
            
def database_done_tasks():
    try:
        conP = sq.connect('done_task.db')
        cursorP = conP.cursor()
        cursorP.execute('''
                        CREATE TABLE IF NOT EXISTS task_done(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           task_name TEXT NOT NULL,
                           des TEXT,
                           completed NUMBER NOT NULL
                        ''')
    except sq.Error as e:
        print(f"ERROR , TIPO DE ERROR: {e}")
    finally:
        if conP:
            conP.commit()
            conP.close()
    
    
        
        