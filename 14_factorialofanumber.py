a=int(input("enter a number to find factorial:"))

fact=1
x=1
while x<=a:
    fact*=x
    x+=1
    
print(f"factorial of {a} is:",fact) 


b=int(input("enter a number:"))

fact=1
for i in range(1,b+1):
    fact*=i


print(f"factorial of {b} is:",fact)     