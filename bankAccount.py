#! usr/bin/env python

"""
bankAccount.py

by David Baylor on 8/27/19

uses python 3

Manages bank accounts.

Could you import a whole folder if you wanted classes from multiple files?

"""


class BankAccount:

    accounts = 0

    def __init__(self):
        self.balance = 0
        BankAccount.accounts += 1
        print("Welcome to your new bank account. Your have {} active account".format(BankAccount.accounts))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry you do not have enough money in your bank account.")
        else:
            self.balance -= amount
            print("You have ${} left in your bank account".format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("You have ${} in your bank account".format(self.balance))

    def vew(self):
        print("You have ${} in your bank account".format(self.balance))
