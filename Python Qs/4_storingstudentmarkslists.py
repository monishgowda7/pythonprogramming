'''note:max(marks)
        min(marks)
        len(marks)ijyhj
        sum(marks)'''


print("creating a marks of 5 students")
marks=[]
for i in range(1,6):
    m=int(input(f"Enter a marks of {i}st student:"))
    marks.append(m)

print("list of 5 student marks=",marks) 
 
print("---highest marks---")    
print("Highest marks is:",max(marks))

print("---lowest marks---")    
print("Lowest marks is:",min(marks))

    
average=sum(marks)/len(marks)
print("---average marks---")
print("average marks:",average)

print("adding one more student marks")
m=int(input(f"Enter a marks of:"))
marks.append(m)
print("After adding the one more student marks:",marks)

print("Removing lowest marks")
marks.remove(min(marks))
print("After removing the lowest marks:",marks)

