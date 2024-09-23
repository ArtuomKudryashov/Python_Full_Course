from BankAccount import BankAccount


class OverdraftAccount(BankAccount):
    def withdraw(self, amount):
        self._balance = self._balance - amount
