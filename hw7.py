#! usr/bin/env python

"""
hw7.py

by David Baylor on 8/11/19

uses python 3

Maneges city_of_seattle_wage_data.csv.

The program runs fine but there are red underlines under open on line 21, FileNotFoundError on line 22, exit on line 25,
and UnicodeDecodeError on line 39. These all have the message 'Unresolved reference' and I am not sure why it is giving
me that error.
"""

import csv
import os

INFILE = "./City_of_Seattle_Wage_Data.csv"

try:
    reader = open(INFILE)
except FileNotFoundError:
    cwd = os.getcwd()
    print(INFILE, "is not in", cwd)
    exit()


try:
    csv_list = []

    for row in csv.reader(reader):
        row = " ".join(row)
        row = row.strip()
        csv_list.append(row)

    print(csv_list)

except UnicodeDecodeError:
    print("Your file is not a csv file.")
