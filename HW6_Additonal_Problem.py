class AccountNotInRangeError(Exception):
    def __init__(self,id,message=''):
        self.id = id
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return self.message
        
class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=-1):
        if annualInterestRate < 0:
            raise AccountNotInRangeError(annualInterestRate,"Annual Interest Rate cant be negative")
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        
    def getId(self):
        return self.__id
        
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setId(self,id):
        self.__id = id
        
    def setBalance(self,balance):
        self.__balance = balance
        
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getMontlyInterestRate(self):
        return(self.__annualInterestRate/12)/100
        
    def getMonthlyInterest(self):
        return self.__balance * self.getMontlyInterestRate()
        
    def deposit(self,Amount):
        if Amount < 0:
            raise AccountNotInRangeError(Amount, "Deposit amount cant be negative")
        self.balance += Amount
    def withdraw(self,Amount):
        if Amount < 0:
            raise AccountNotInRangeError(Amount,"Amount to Withdraw cant be negative")
        self.balance -= Amount
        
def main():
    accountA = Account(0,100,-1)
    accountA.id = 1122
    accountA.balance = 20000
    accountA.annualInterestRate = 0.045
    print(accountA)
    accountA.withdraw(2500)
    accountA.deposit(-80)
    print(accountA)
    print(accountA.getMonthlyInterest()) 

main()
