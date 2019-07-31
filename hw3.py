#! usr/bin/env python

'''
hw3.py
Makes a list of household items and their prices on a separate file.
By David Baylor on 7/16/19
using python 3

How do I get rid of the extra line that prints inbetween the items?
'''


with open(r".\HomeInventory.txt", "a+") as fh:  #opens HomeInventory.txt
    item = input("Name a household item. ")  #asks for the items name and price
    price = input("how much does that cost. $")

    outlines = [item, " $", price, "\n"]

    fh.writelines(outlines)  #adds the new item to the list
    fh.seek(0)  #goes to the top of HomeInventory.txt

    line = fh.readline()
    while line:  #prints each line and stops after all the lines have been printed.
        print(line)
        line = fh.readline()
