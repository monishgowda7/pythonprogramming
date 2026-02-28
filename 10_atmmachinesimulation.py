class ATM:
    def __init__(self,pin,balance=0):
        self.pin=pin
        self.balance=balance
       
        
    def verify(self,entered_pin):
        if entered_pin==self.pin:
            return True
        else:
            return False
        
    def checkbal(self):
        return f"Your current balance is :{self.balance}"
    
    def withdraw(self,amount):
        if amount>self.balance:   
            print("insufficint balance")   
            
        elif amount<=0:
            print("invalid amount")      
        
        else:
            self.balance-=amount
            print("amount id sucessfully withdrawn,Collect your cash")    
            print(f"after withdrawn BALANCE IS :{self.balance}")
            
    def deposit(self,entre_amount):
        if entre_amount>0:
            print("Amount is succesfully deposited to your account")
            self.balance+=entre_amount
            print(f"After deposit balance is {self.balance}")   
            
        elif entre_amount<0:
            print("invalid amount")
            
        else:
            print("hey u entered amount is zerp")          
            
            
            
atm=ATM(7777,100000)    
print("you have only 3 attempts to enter a password")
attempt=0
max_attempt=3
while attempt < max_attempt:
    entered_pin=int(input("enter a pin:"))
    
    if atm.verify(entered_pin):
        print("Successfully LOGINED")
        break
        
    else:
        attempt+=1
        print("incorrect password Attempts left:",max_attempt-attempt)
   

if atm.verify(entered_pin):
    while True:
        print("1.CHECK BALANACE")       
        print("2.DEPOSIT")       
        print("3.WITHDRAW")       
        print("4.EXIT")       
        
        n=int(input("ENTER a option:"))
        
        if n==1:
            print(atm.checkbal())
            

        elif n==2:
            entre_amount=int(input("enter a amount to deposit:"))
            atm.deposit(entre_amount) 
             
            
        elif n==3:
            amount=int(input("enter a amount to withdraw:"))
            atm.withdraw(amount)
            
        elif n==4:
            print("Sucessfully exited") 
            break   
            
        else:
            print("invalid option")
            
            
elif attempt==max_attempt:
    print("WRONG PIN,Too many failed attempts,ACCOUNT LOCKED")           