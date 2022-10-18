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
    
print("Your score is " + str(score))
