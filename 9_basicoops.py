class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def intro(self):
        return f"my name is {self.name},and i scord {self.marks} in maths"    


stud1=student("monish",100)        
print(stud1.name)
print(stud1.marks)
print(stud1.intro())





class arearect:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        return (self.length*self.width)
    
    


a=arearect(2,5)    
print("area of rectanmgle:",a.area())



