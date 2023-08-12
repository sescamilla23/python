class Account:

    def __init__(self, name: str):
        """Initialization of account with name and balance of 0"""
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Adds amount to account balance
        :param amount: amount to be deposited.
        :return: True if deposit is successful, otherwise false
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        subtracts the amount from account balance
        :param amount: amount to be withdrawn.
        :return: True if withdraw is successful, otherwise false
        """
        if amount <= 0 or self.__account_balance < amount:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """Returns account balance total"""
        return self.__account_balance

    def get_name(self) -> str:
        """Returns account name"""
        return self.__account_name
