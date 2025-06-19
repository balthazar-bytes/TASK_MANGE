import sqlite3 as sq
import database

def database_create():
    database.task_list_create()

def menu():
    print(
        f"TASK MENU\n1) Task list\n2) Add new task\n3) Task update section\n4) List of tasks finished\n5) List of task in progress\n6) Delete task"
    )

def selector():
    while True:
        try:
            option = int(input("ingresar una opcion: "))
            if 1 <= option <= 6:
                return option
            else:
                print("Ingresar una opcion valida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def task_list():
    con = sq.connect('task_list.db')
    cursor = con.cursor()
    cursor.execute('''
                   SELECT * FROM task
                   ''')
    tasks = cursor.fetchall()
    if not tasks:
        print("You dont have any task")
    else:
        print('---Task list---')
        for task in tasks:
            id,name,des,status = task
            if status == 0:
                status = 'Inclompleted'
            elif status == 1:
                status == 'In progress' 
            else:
                status == 'Done'
            print(f"------------------\nId = {id}\nName: {name}\nDescription: {des}\nStatus: {status}")
            
    con.close()        
    
    
def create_task():
    try:
        con = sq.connect('task_list.db')
        cursor = con.cursor()
        task = input('insert task name: ')
        des = input('descrive your task: ')
        cursor.execute('''
                    INSERT INTO task (task_name,des) VALUES(?,?)
                    ''',(task,des))
    except sq.Error as e:
        print(f"Error: {e}")
    finally:
        con.commit()
        con.close()
        
        
def update_task():
    try:
        con = sq.connect('task_list.db')
        cursor = con.cursor()
        try:
            task =  int(input('insert task ID:'))
            status = int(input('insert task status(0 = not in progress 1  = in progress ,2 = done): '))
            while status < 0 or status > 2:
                print('invalid entry: out of range')
                status = int(input('insert task status(0 = not in progress 1  = in progress ,2 = done): '))
        except ValueError:
            print('insert a number')
        cursor.execute(''' UPDATE task SET completed = ? WHERE id = ?  ''',(status,task))
        if cursor.rowcount == 0:
            print('task ID doesnt exists')
        else:
            print('The task was updated successfully.')
    except sq.Error as e:
        print(f'Sqlite error : {e}')
    finally:
        con.commit()
        con.close()
        
        
def task_in_progress():
    try:
        con1 = sq.connect('task_list.db')
        cursor_main = con1.cursor()
        taskP = cursor_main.execute(''' SELECT * FROM task WHERE completed = 1''')
        for task in taskP:
            
            print(f'f"------------------\nId = {task[0]}\nName: {task[1]}\nDescription: {task[2]}\nStatus: In progress')
    except sq.Error as e:
        print(f'Error: {e}')
    finally:
        con1.commit()
        con1.close()
        
        
        
def task_done():
    try:
        con1 = sq.connect('task_list.db')
        cursor_main = con1.cursor()
        taskP = cursor_main.execute(''' SELECT * FROM task WHERE completed = 2''')
        for task in taskP:
            
            print(f'f"------------------\nId = {task[0]}\nName: {task[1]}\nDescription: {task[2]}\nStatus: Done')
    except sq.Error as e:
        print(f'Error: {e}')
    finally:
        con1.commit()
        con1.close()
        
def task_delete():
    try:
        con1 = sq.connect('task_list.db')
        cursor_main = con1.cursor()
        try:
            task = int(input('Insert task ID: '))
        except ValueError:
            print('Insert a valid number')
            return
        confirm = input('Are you sure?(yes-no): ').strip().lower()
        if confirm not in ('yes', 'no'):
            print('This is not a valid answer. Please type "yes" or "no".')
            return
        if confirm == 'yes':
            cursor_main.execute('''DELETE FROM task WHERE id = ?''', (task,))
            if cursor_main.rowcount == 0:
                print('Task ID doesnt exist')
            else:
                print('Task Deleted')
        else:
            return
    except sq.Error as e:
        print(f'Error: {e}')
    finally:
        con1.commit()
        con1.close()
        
                
    
        
        
        
        