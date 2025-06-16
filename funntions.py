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

    
    
    
