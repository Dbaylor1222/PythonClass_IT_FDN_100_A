#! usr/bin/env python

"""
hw4.py

Asks for a household item's name and price and stores that in a tuple. When you leave the program it asks if you would
like to save the information in a file.

written by David Baylor on 7/23/2019
using python 3
"""

item = ()
list = ()

while True:
    # Asks the user if they want to add another item to the list. The greeting is different if there are no items in the list.
    if not item:
        greeting = "Would you like to add an item to the list? "
    else:
        greeting = "would you like to add another item to the list? "

    # If the answer is yes it asks the user for the name and price of the item.
    if input(greeting).lower() == "yes":
        itemName = input("Name a household item: ")
        itemCost = input("How much does that cost? $")

        # Adds the item to a running list.

        item = (itemName, itemCost)
        if not list:
            list = (item,)
        else:
            list = list + (item,)

        print(list)

    # Asks the user if they want to save the list to homeInventory2.txt when the close the program.
    elif input("Would you like to save your items to homeInventory2.txt? ").lower() == "yes":
        print(list)
        with open(r".\HomeInventory2.txt" , "a") as fh:
            # Adds the list to homeInventory2.txt.
            for i in list:
                fh.write(i[0] + ", " + i[1] + "\n")
            print("Your items have been successfully added to homeInventory2.txt.")
        break
    else:
        input("Press enter to exit.")
        break
