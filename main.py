class Bankaccount:
    next_account_number=1001
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance
        self.account_number=Bankaccount.next_account_number
        Bankaccount.next_account_number+=1
        self.transactions=[]
    def deposite(self,amount1):
            if amount1>0:
                 print("amount should be +ve")
                 self.__balance=self.__balance+amount1
                 print("Deposite is successfully!")
            else:
                 print("Insufficent money")
            self.transactions.append("Deposite:1000")
            self.transactions.append(f"Deposite:{amount1}")      
    def withdraw(self,amount1):
         if amount1<=0:
              print("amount should be positive!")
         elif amount1<=self.__balance:
              self.__balance=self.__balance-amount1
              print("withdraw Successfully!")
         else:
              print("there is no money inside the acount1")
         self.transactions.append(f"withdrawal:{amount1}")
    def check_balance(self):
         print(self.__balance)
    def display_detail(self):
         print("Account Holder name $:",self.account_holder)
         print("Balnce $:",self.__balance)
         print("Account number $:",self.account_number)
    def show_transactions(self):
         print("Transaction History for:",self.account_holder)
         for transaction in self.transactions:
              print(transaction)

    
account1=Bankaccount("shyam",8000)
account2=Bankaccount("ravi",5000)
account1.deposite(2000)
account1.withdraw(3000)

account1.withdraw(-500)
account2.deposite(1000)
account1.check_balance()
account2.check_balance()
account1.display_detail()
account2.display_detail()
account1.deposite(-1000)
account2.deposite(0)
print(account1.account_number)
print(account2.account_number)
print(account1.transactions)
print(account2.transactions)
account1.show_transactions()
account2.show_transactions()

#practising git changes

