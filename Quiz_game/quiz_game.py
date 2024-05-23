print("Welcome to computer quiz!")

name = input("What's your name?")

playing = input("Do you want to play?")

if playing != "yes":
    quit()

print("Let's play")
score = 0
answer = input("What does RAM stands for? ")

if answer.lower() == "random access memory":
    print("Great job!")
    score += 1
else:
    print("Incorrect")

answer2 = input("What does CPU stands for? ")

if answer2.lower() == "central processing unit":
    print("Great job!")
    score += 1
else:
    print("Incorrect")

answer3 = input("What does PSU stands for? ")

if answer3.lower() == "power supply":
    print("Great job!")
    score += 1
else:
    print("Incorrect")

answer3 = input("What does PC stands for? ")

if answer3.lower() == "personal computer":
    print("Great job!")
    score += 1
else:
    print("Incorrect")


print("You got "+ str(score) + " questions correct,"+ name)