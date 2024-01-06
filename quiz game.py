print("Welcome to my computer quiz game")
begin = input("Do you want to play?")
if begin.lower() == "yes":
    print("okay let's begin: ")
else:
    quit()    
score = 0

answer = input("what does CPU stand for:  ")    
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect") 
       
answer = input("what does RAM stand for:  ")    
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect") 
    
answer = input("what does ROM stand for?  ")
if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("incorrect")     
answer = input("what does PSU stand for?")       
if answer.lower() == "power supply unit":
    print("correct")
    score += 1
else:
    print("incorrect")    

if score >= 2:
        print("you got " +  str(score) + " questions correct!")
else:
    print("you got "  + str(score)  +  " question correct")          
print("you had  " + str(score/4 * 100) + "%")