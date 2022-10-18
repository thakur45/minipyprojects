from tkinter.messagebox import YES


print("Welcome to computer quiz")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()
print("Okay, lets goo !!")
score = 0
answer = input("What does CPU stands for ? ")
if answer.lower() == "central processing unit":
    print("Correct !")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stands for ? ")
if answer.lower() == "random access memory":
    print("Correct !")
    score += 1
else:
    print("Incorrect")

answer = input("What does ROM stands for ? ")
if answer.lower() == "read only memory":
    print("Correct !")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stands for ? ")
if answer.lower() == "graphic processing unit":
    print("Correct !")
    score += 1
else:
    print("Incorrect")

answer = input("What does WWW stands for ? ")
if answer.lower() == "world wide web":
    print("Correct !")
    score += 1
else:
    print("Incorrect")

    
print("Your score is " + str(score))
print("Your " + str((score/5)*100) + "%" " of answers correct")
