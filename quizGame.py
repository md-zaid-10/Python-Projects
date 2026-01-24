print("Welcome to my Computer Quiz")

playing = input("Do you want to play the game ? (Yes/No)")


if playing != "yes":
    quit()

print("Okay lets play !")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does GPU stand for ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

print("You got " , score , " quesions correct!" )
print("You got " , ((score/4)*100) , "%." )