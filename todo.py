import time


def print_stop(text):
    time.sleep(0.5)
    print(text)


tasks = {

}


def add_task():
    print("""To add a Task u must 
    specify three things:
        -Task Name
        -Task Type is it an important task or mid important task
        -Task Description""")
    while True:
        global task_name
        task_name = input("First Write The task Name: ")
        global task_type
        task_type = input("Write the task Type (Important or Mid Important): ")
        global task_description
        task_description = input("Write the task Description: ")
        tasks[task_name] = {
            "Task Type": task_type,
            "Task Description": task_description,
            "progress": False
        }
        print(f"Task added successfully")
        show = input("Do U want to see Your Tasks (Y/N)?: ")

        if show == 'y' or show == 'Y':
            for task, value in tasks.items():
                print(f"Task Name: {task}")
                print(f"Task Type: {value['Task Type']}")
                print(f"Task Description: {value['Task Description']}")
                print(f"progress: {value['progress']}")
                print('-'*20)
            print_stop("Todo list is showed")
            break

        elif show == 'n' or show == 'N':
            print_stop("Thanks for usingg Our ToDo list")
            break


def compeleted_task():

    while True:
        task_name2 = input("write the name of the task that U finished it ")
        if task_name2 in tasks:
            tasks[task_name2]['progress'] = True
            print(f"Good Job Bro of finishing {task_name2}")
            break
        else:
            print(f"Bro check the Name of the this task {task_name2}")


def main():
    while True:
        print("Hi to our ToDo list !")
        print("If u want to add a task type 1")
        print("Make a task as a completed type 2")
        print("Show Tasks type 3")
        print("Exit type 4")
        num = int(input("what will u choose"))
        if num == 1:
            add_task()
        elif num == 2:
            compeleted_task()
        elif num == 3:
            for task, value in tasks.items():
                print('-'*50)
                print(f"Task Name: {task}")
                print(f"    -Task Type: {value['Task Type']}")
                print(f"    -Task completed: {value['progress']}")
                print(f"    -Task description: {value['Task Description']}")
        elif num == 4:
            print("Thank u bro For using Our app")
            break


main()
