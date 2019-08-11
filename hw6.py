#! usr/bin/env python

'''
hw6.py
By David Baylor on 8/7/19
maneges a to do list using dictionaries, lists, and functions.
uses python 3

Are you supposed to put the main body of the program in a 'main' function or not?
'''

INFILE = r".\Todo.txt"
# read in ToDo.txt here using readlines
with open(INFILE, 'r') as todo_file:
    lines = todo_file.readlines()
# create empty dictionary to store data as we loop
task_dict = {}
for line in lines:
   item = line.split(",")
   task = item[0]  #split the line and pull out task by index
   priority = item[1]  #split the line and pull out priority by index
   task_dict[task] = priority  # add line to add new key to a dictionary here using task ask key and priority


def view_items(input_dict):
    """function to view items currently in dictionary"""
    for item in input_dict:
        print(item + "," + input_dict[item])
    input("\n\npress enter to go back to the main menu.")


def add_task(input_dict):
    """add new tasks to dictionary"""
    key = input("What task would you like to add? ")
    while key in input_dict or "," in key:
        key = input("The task must be unique and have no commas. What task would you like to add? ")
    value = input("What is the priority? ")
    input_dict[key] = value
    print(key + "," + input_dict[key] + " has been added to the list.")
    input("\n\npress enter to go back to the main menu.")
    return input_dict


def remove_task(input_dict):
    """remove tasks from dictionary"""
    remove_key = input("Enter the task name to remove: ")
    if remove_key in input_dict:
        remove_value = input_dict[remove_key]
        del input_dict[remove_key]
        print(remove_key + "," + remove_value + " has been removed from the list")
    else:
        print("That task is not in the list")
    input("\n\npress enter to go back to the main menu.")
    return input_dict


def save_todo(input_dict):
    """save items to file"""
    with open(INFILE, "w") as todo_file:
        for item in input_dict:
            todo_file.write(item + "," + input_dict[item] + ",\n")
    print("your list has been saved to todo.txt")


while(True):
    print ("""
    To do list 
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Choice 1 -Show the current items in the table
    if strChoice.strip() == '1':
        view_items(task_dict)

    # Choice 2 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        task_dict = add_task(task_dict)

     # Choice 3 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        task_dict = remove_task(task_dict)

     # Choice 4 - Save tasks to the ToDo.txt file
    elif strChoice.strip() == '4' :
        save_todo(task_dict)

     # Choice 5- end the program
    elif strChoice == '5':
        break #and Exit the program
