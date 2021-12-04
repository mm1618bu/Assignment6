class Account:
   # Deinfine the Class Account
   def __init__(self, id, balance = 100, annualInterestRate = 0): #set id, balance, annualInterestRate
       self.__id = id
       self.__balance = balance
       self.__annualInterestRate = annualInterestRate

   def getId(self): #return account id
       return self.__id

   def getBalance(self): # return current balance
       return self.__balance

   def getAnnualInterestRate(self): # return interest rate annually
       return self.__annualInterestRate

   def getMonthlyInterestRate(self): # determine monthly interest rate
       return self.__annualInterestRate / 12

   def setPreviousPrice(self, previousPrice): # define the previous balance
       self.previousPrice = previousPrice

   def setCurrentPrice(self, currentPrice): # define the current balance
       self.currentPrice = currentPrice

   def withdraw(self, amount): # amount to withdraw
       self.__balance -= amount

   def deposit(self, amount): # amount to deposit
       self.__balance += amount

   def getMonthlyInterest(self): # return the monthly interest
       return self.__balance * self.getMonthlyInterestRate()

def main():
   # Creating ten accounts in a list with the ids 0 , 1 , ..., 9 , and an initial balance of $100
  
   # List of accounts
   accounts = [];
  
   # Creating ten accounts
   for i in range(0, 10):
       account = Account(i, 100.0);
       accounts.append(account);
      
      
   while True:
  
       # Reading id from user
       id = int(input("\n Enter account id: "));
      
       # Loop till id is valid
       while id < 0 or id > 9:
           id = int(input("\n Invalid Id.. Re-enter: "));
       # Iterating over game  
       while True:
          
           # Printing menu
           print("\n 1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ");
          
           # Reading selection
           selection = int(input("\n Enter your selection: "));
          
           # Getting account object
           for acc in accounts:
               # Comparing account id
               if acc.getId() == id:
                   accountObj = acc;
                   break;
          
           # View Balance
           if selection == 1:
               # Printing balance
               print(accountObj.getBalance());
              
           # Withdraw  
           elif selection == 2:
               # Reading amount
               amt = float(input("\n Enter amount to withdraw: "));
               # Calling withdraw method
               accountObj.withdraw(amt);
               # Printing updated balance
               print("\n Updated Balance: " + str(accountObj.getBalance()) + " \n");
              
           # Deposit  
           elif selection == 3:
               # Reading amount
               amt = float(input("\n Enter amount to deposit: "));
               # Calling deposit method
               accountObj.deposit(amt);
               # Printing updated balance
               print("\n Updated Balance: " + str(accountObj.getBalance()) + " \n");
          
           # Any other choice
           else:
               break;
          
# Main function          
main()
