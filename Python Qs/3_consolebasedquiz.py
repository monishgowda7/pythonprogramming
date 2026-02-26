a=input("enter your full name:")
print("WELCOME to quiz")
print("1.START QUIZ")
print("2.INSTRUCTIONS")
print("3.EXIT")
b=int(input("Enter a option:"))
marks=0
match(b):
    case(1):
        print("Q1.TOTAL ECONOMY OF INDIA")
        print("1.1T")
        print("2.60T")
        print("3.2T")
        print("4.4.3T")
        c=int(input("ANSWER:"))
        while(c>4 or c<0):
            print("invalid option:enter within(0-4)")
            c=int(input("ANSWER:"))
            
        if(c==4):
            marks+=5
        elif(c==1 or c==2 or c==3):
            marks+=-2
        elif(c==0):
            marks+=0

                   
        print("Q2.who is PRIME MINISTER  of india")
        print("1.narendra modi")
        print("2.iam")
        print("3.you")
        print("4.i dont know")
        c=int(input("ANSWER:"))
        while(c>4 or c<0):
            print("invalid option:enter within(0-4)")
            c=int(input("ANSWER:"))
            
        if(c==1):
            marks+=5
        elif(c==2 or c==3 or c==4):
            marks+=-2
        elif(c==0):
            marks+=0
           
                   
        print("Q3.what is QUANTUM MECHANICS")
        print("1.deals with magnetic field")
        print("2.deals with atoms,frequency,wave")
        print("3.deals with current")
        print("4.i dont know")
        c=int(input("ANSWER:"))
        while(c>4 or c<0):
            print("invalid option:enter within(0-4)")
            c=int(input("ANSWER:"))   
            
        if(c==2):
            marks+=5
        elif(c==1 or c==3 or c==4):
            marks+=-2      
        elif(c==0):
            marks+=0
         
            
        print("Q4.which is the tallest statue")
        print("1.statue of unity")
        print("2.spring temple buddha")
        print("3.sendai daikannon")
        print("4.statue of liberty")
        c=int(input("ANSWER:"))
        while(c>4 or c<0):
            print("invalid option:enter within(0-4)")
            c=int(input("ANSWER:"))
            
        if(c==1):
            marks+=5
        elif(c==4 or c==2 or c==3):
            marks+=-2
        elif(c==0):
            marks+=0
                    
        
        print("quiz completed")
        print(f"your total score in quiz is :{marks}")
             
         
    case(2):
        def instructions():
            print("there will be 4 questions")
            print("each question has 4 option(1,2,3,4)")
            print("PRESS 0(zero) to skip the question")
            print("FOR CORRECT ANSWER---->+5 marks ")
            print("FOR WRONG ANSWER---->-2 marks")
        instructions()       
        
    case(3):
        print("succesfully exited")        
            
    case _:
        print("invalid option")        