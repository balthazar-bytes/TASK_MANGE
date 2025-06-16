from funntions import menu,database_create,selector,task_list,create_task
import sqlite3

database_create()

while True:
    menu()
    opcion = selector()
    if opcion == 1:
        task_list()
    elif opcion == 2:
        create_task()
    