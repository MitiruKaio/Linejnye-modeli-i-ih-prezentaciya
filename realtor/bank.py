from client import Client
from account import Account


class Bank:
    def __init__(self):
        self.__accounts = []

    def add_account(self, client: Client) -> Account:
        for account in self.__accounts:
            if account.client is client:
                raise ValueError("Client already has an account!")

        account = Account(client)
        self.__accounts.append(account)
        return account

    def __str__(self):
        if not self.__accounts:
            return "Bank has no clients"

        return "\n".join(str(account) for account in self.__accounts)
