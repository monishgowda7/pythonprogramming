a=input("enter a word:").lower()
program={}
for i in a:
    if i in program:
        program[i]+=1
        
    else:
        program[i]=1
        
        
for keys ,values in program.items():
    print(keys,":",values)
            