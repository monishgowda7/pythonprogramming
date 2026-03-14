import random
import string

a=int(input("Enter length of passowrd:"))
password=string.ascii_letters+string.digits+string.punctuation

password_generated=""
for i in range(1,a+1):
    password_generated+=random.choice(password)
    
print("Generated password:",password_generated)    
    
