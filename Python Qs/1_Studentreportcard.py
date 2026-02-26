name=input("enter your name:")
usn=input("enter your usn:")
print("enter 5 subject marks:")
m1=int(input("enter marks of 1st subject:"))
m2=int(input("enter marks of 2st subject:"))
m3=int(input("enter marks of 3st subject:"))
m4=int(input("enter marks of 4st subject:"))
m5=int(input("enter marks of 5st subject:"))

total=m1+m2+m3+m4+m5
print(f'your total marks is={total}')
average=(total/5)
print(f"your average marks is={average}")


if average>=90:
    grade="A"
    
elif average>=80:
    grade='B'    
elif average>=70:
    grade ="C"   
elif average>=60:
    grade= "D"  
elif average>=50:
    grade ="E"  
elif average<=50:
    grade= "F"   
else:
    grade="g"    
        
        
if m1<40 or m2<40 or m3<40 or m4<40 or m5<40:
    status="FAIL"
else:
    status="PASS"
        
    

print("----------------------------------")
print("       student report card        ")
print("----------------------------------")

print(f"NAME       :{name}")
print(f"usn        :{usn}")
print(f"total marks:{total}")
print(f"average    :{average}")
print(f"grade      :{grade}")

print("----------------------------------")
print(f"status     :{status}")
print("----------------------------------")