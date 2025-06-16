import sqlite3 as sq
import database

def database_create():
    database.task_list_create()
    database.task_in_progress()
    database.database_done_tasks()

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