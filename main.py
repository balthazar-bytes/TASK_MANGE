from funntions import menu,database_create,selector,task_list,create_task,update_task,task_in_progress,task_done
import sqlite3

database_create()
'''        f"TASK MENU
1) Task list
2) Add new task
3) Task update section
4) List of tasks finished
5) List of task in progress
6) Delete task"
'''
while True:
    menu()
    opcion = selector()
    if opcion == 1:
        task_list()
    elif opcion == 2:
        create_task()
    elif opcion == 3:
        update_task()
    elif opcion == 4:
        task_done()
    elif opcion == 5:
        task_in_progress()
    elif opcion == 6:
        
    