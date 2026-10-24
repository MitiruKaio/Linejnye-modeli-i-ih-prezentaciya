from math import isfinite


class Account:
    default_amount = 0

    def __init__(self, client, amount=default_amount):
        self.__client = client
        self.amount = amount

    @property
    def client(self):
        return self.__client

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if not isfinite(value) or value < 0:
            raise ValueError("Balance must be a finite non-negative number")
        self.__amount = value

    def __str__(self):
        return f"Account owner: {self.client.name}, amount: {self.amount}"

    def __iadd__(self, money):
        if not isfinite(money) or money < 0:
            raise ValueError("Deposit must be a finite non-negative number")
        self.amount += money
        return self

    def __isub__(self, money):
        if not isfinite(money) or money < 0:
            raise ValueError("Withdrawal must be a finite non-negative number")
        if self.amount - money < 0:
            print("Account cannot go below zero!")
        else:
            self.amount -= money
        return self
