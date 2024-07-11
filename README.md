# ToDo List Application

This is a simple command-line ToDo list application written in Python. It allows you to add tasks, mark them as completed, and view your task list.

## Features

- Add tasks with a name, type, and description.
- Mark tasks as completed.
- View all tasks with their details.
- Simple and interactive command-line interface.

## How to Use

1. **Run the Application**:
   ```sh
   python todo_list.py
Main Menu:

You will be greeted with the main menu options:
css
Copy code
Hi to our ToDo list!
If u want to add a task type 1
Make a task as a completed type 2
Show Tasks type 3
Exit type 4
Add a Task:

Type 1 to add a task.
Follow the prompts to enter the task name, type, and description.
Example:
mathematica
Copy code
First Write The task Name: Buy Groceries
Write the task Type (Important or Mid Important): Important
Write the task Description: Buy fruits and vegetables from the market.
Task added successfully
Do U want to see Your Tasks (Y/N)?: Y
Mark a Task as Completed:

Type 2 to mark a task as completed.
Enter the name of the task you want to mark as completed.
Example:
arduino
Copy code
write the name of the task that U finished it: Buy Groceries
Good Job Bro of finishing Buy Groceries
Show Tasks:

Type 3 to view all tasks.
The task list will display the task name, type, description, and completion status.
Example:
yaml
Copy code
Task Name: Buy Groceries
    -Task Type: Important
    -Task completed: True
    -Task description: Buy fruits and vegetables from the market.
Exit the Application:

Type 4 to exit the application.
Example:
arduino
Copy code
Thank u bro For using Our app
Example Usage
sh
Copy code
$ python todo_list.py
Hi to our ToDo list !
If u want to add a task type 1
Make a task as a completed type 2
Show Tasks type 3
Exit type 4
what will u choose1
To add a Task u must 
specify three things:
    -Task Name
    -Task Type is it an important task or mid important task
    -Task Description
First Write The task Name: Finish Homework
Write the task Type (Important or Mid Important): Important
Write the task Description: Complete math and science homework.
Task added successfully
Do U want to see Your Tasks (Y/N)?: Y
Task Name: Finish Homework
Task Type: Important
Task Description: Complete math and science homework.
progress: False
--------------------
Todo list is showed
Thank u bro For using Our ToDo list
Requirements
Python 3.x
