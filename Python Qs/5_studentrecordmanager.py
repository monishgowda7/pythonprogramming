record=[]
print(f"enter a details of student")
for i in range(1,4):
    
    name=input(f"enter {i}st student name:")
    id=int(input(f"enter your ID {name}:")) 
    info=(name,id)
    
    subject=set()
    s=int(input(f"enter how many subjects:")) 
    marks={}
    for j in range(s):
        n=input(f"Enter a {j+1}st subject=")
        subject.add(n)
        
          
        p=int(input(f"enter a marks of {n}="))
        marks[n]=p
         
    student_record=(info,subject,marks)
    record.append(student_record)
    print(record)    