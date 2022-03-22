class BankAccount:

    def __init__(self, cbu):
        self.__balance = 0
        self.__cbu = cbu

    def deposit(self, amount):
        success = True
        if amount > 0:
            self.__balance += amount
        else:
            success = False
        return success

    def withraw(self, amount):
        success = True
        if amount > 0:
            self.__balance -= amount
        else:
            success = False
        return success

    def getBalance(self):
        return self.__balance

    def getCBU(self):
        return self.__cbu

    def __str__(self):
        return "CBU: " + str(self.__cbu) + "\n" + "Balance: " + str(self.__balance)
