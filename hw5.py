#! usr/bin/env python

'''
hw5.py
By David Baylor on 7/29/19
maneges a to do list using dictionaries and lists.
uses python 3

when you are writing to a file what is the best way to go to a new line without the '\n' showing up when you read the
file?
'''

infile = r".\Todo.txt"
# read in ToDo.txt here using readlines
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()
# create empty dictionary to store data as we loop
task_dict = {}
for line in lines:
   item = line.split(",")
   task = item[0]  #split the line and pull out task by index
   priority = item[1]  #split the line and pull out priority by index
   task_dict[task] = priority  # add line to add new key to a dictionary here using task ask key and priority


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
        for item in task_dict:
            print(item + "," + task_dict[item])
        input("\n\npress enter to go back to the main menu.")

    # Choice 2 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        key = input("What task would you like to add? ")
        while key in task_dict or "," in key:
            key = input("The task must be unique and have no commas. What task would you like to add? ")
        value = input("What is the priority? ")
        task_dict[key] = value
        print(key + "," + task_dict[key] + " has been added to the list.")
        input("\n\npress enter to go back to the main menu.")

     # Choice 3 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        remove_key = input("Enter the task name to remove: ")
        if remove_key in task_dict:
            remove_value = task_dict[remove_key]
            del task_dict[remove_key]
            print(remove_key + "," + remove_value + " has been removed from the list")
        else:
            print("That task is not in the list")
        input("\n\npress enter to go back to the main menu.")


     # Choice 4 - Save tasks to the ToDo.txt file
    elif strChoice.strip() == '4' :
        with open(infile ,"w") as todo_file:
            for item in task_dict:
                todo_file.write(item + "," + task_dict[item] + ",\n")
        print("your list has been saved to todo.txt")

#     # Choice 5- end the program
    elif (strChoice == '5'):
        break #and Exit the program
