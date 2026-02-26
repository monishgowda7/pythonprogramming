print('welcome to indian bank')
a=input('enter your name:')
print("1.DEPOSIT")
print("2.WITHDRAW")
print("3.CHECK BALANCE")
print("4.EXIT")
s=int(input("ENTER a option:"))
match(s):
    case(1):
        m=int(input("enter a amount to deposit:"))
        if (m>0):
            def deposit(m):
                return int(1000+m)
            print("deposit sucessful")
            print("CURRENT BALANCE:",deposit(m))
            print("THANK YOU for depositing an amount")
            
        else:
            print("invalid amount")
                
                
        
    case(2):
        print("CURRENT BALANCE IS:1000")
        n=int(input("enter a amount to WITHDRAW:"))
        if(n<=500):
            print(f"AMOUNT {n} is succesfully withdrawn")  
            print("collect your cash in counter")  
            
        else:
            print("YOU entered more than 500rs,our bank balance should maintain more than 500.withdraw failed")  
            
                
                
    case(3):
        print("CURRENT BALANCE IS :1000")
        
        
    case(4):
        print("thank you")
        
        
    case _:
        print("invalid choice")
            
                        
        
