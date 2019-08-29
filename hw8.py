#! usr/bin/env python

"""
bankAccount.py

by David Baylor on 8/27/19

uses python 3

The UI to bankAccount.py.

Could you import a whole folder if you wanted classes from multiple files?

"""

from bankAccount import BankAccount  # imports the class
myAccount = BankAccount()
myAccount.vew()

choice = ""

while choice != "D":
    choice = input("""
    What would you like to do?
    A) Vew account balance.
    B) Make a deposit. 
    C) Withdraw money.
    D) Quit
    """)

    choice = choice.upper()

    # views account
    if choice == "A":
        myAccount.vew()

    # Makes a deposit
    elif choice == "B":
        amount = int(input("How much would you like to deposit? $"))
        myAccount.deposit(amount)

    # Withdraws money
    elif choice == "C":
        amount = int(input("How much would you like to withdraw? $"))
        myAccount.withdraw(amount)

    # exits the program
    elif choice == "D":
        pass

    else:
        print("Please pick either A,B,C, or D.")
