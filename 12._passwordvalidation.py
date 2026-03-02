def password(p):
    if(len(p)<4):
        print("Weak password,try again")
        
        
    digit=False
    char=False
    for i in p:
        if i.isdigit():
            
            digit=True
        
                
        if i.isupper():   
            char=True

                        
    if not digit:
        print("Add atleast on digit in password") 
                    
                        
    if not char:
        print("Add atleast one upper case alphabeat in password")     
            
    print("password verification complete")    
      
p=input("enter a password:")    
a=password(p)   
print(a)
 
            
            
    
        
    