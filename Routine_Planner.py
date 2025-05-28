import os

print("-------- Routine Planner --------")
print()
print("Add , View , Mark , Delete , Exit")
print()
option = input("Choose an option :")

# add
if option.lower() == "add":
    print()
    task_num = int(input("Enter how many tasks you want to add :"))
    print()
    for i in range(1, task_num + 1):
        task = input(f"Enter task {i} :")
        with open("data.txt", "a") as f:
            f.write(f"[ ] {task}\n")
    print()
    print("The data is successfully added...")

# view
elif option.lower() == "view":
    print()
    if not os.path.exists("data.txt"):
        print("No data file found.")
    else:
        with open("data.txt", "r") as f:
            data = f.read()
            print("    SAVED DATA    ")
            print()
            print(data)
    print()

# mark
elif option.lower() == "mark":
    mark_task = input("Enter the task to update: ")
    print()
    print("  WHAT DO YOU WANT TO MARK IT AS?  ")
    print("   Completed , Delayed , Skipped   ")
    print()
    task_specs = input("Choose an option: ").lower()
    updated_tasks = []
    found = False

    with open("data.txt", "r") as f:
        tasks = f.readlines()

    for task in tasks:
        if mark_task.lower() in task.lower():
            found = True
            if task_specs == "completed":
                updated_task = task.replace("[ ]", "[ COMPLETED ]")
            elif task_specs == "delayed":
                updated_task = task.replace("[ ]", "[ DELAYED ]")
            elif task_specs == "skipped":
                updated_task = task.replace("[ ]", "[ SKIPPED ]")
            else:
                print("Invalid mark option.")
                updated_task = task
            updated_tasks.append(updated_task)
        else:
            updated_tasks.append(task)

    with open("data.txt", "w") as f:  
        f.writelines(updated_tasks)

    if found:
        print("Task updated successfully!")
    else:
        print("Task not found.")

#delete
elif option.lower() == "delete":
    del_data = input("Enter the task you want to delete :")
    print()
    if not os.path.exists("data.txt"):
        print()
        print("No data file found.")
    else:
        with open("data.txt", "r") as f:
            datas = f.readlines()
            for data in datas:
                with open("data.txt", "w") as file:  
                    if del_data.lower() not in data.lower():    
                        file.writelines(data)
                    elif del_data.lower() == data.lower():
                        pass
            print()
            print(" TASK IS DELETED ")

#Exit
elif option.lower() == "exit":
    print()
    print(" Thanks for using our routine planner ") 

# Incorrect input  
else:
    print()
    print(" Invalid input, kindly enter correct data ")                        




