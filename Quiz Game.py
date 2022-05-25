print("Welcome to my quiz!")

playing = input("Continue?\n")

score = 0

if playing.lower() != "yes":
    print("Goodbye")
    quit()
else:
    print("Lets Begin!")

answer = input("Which sea creature has three hearts?\n")
if answer == "octopus":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("How many bones does an adult human have?\n")
if answer.lower() == "206":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the Italian word for pie?\n")
if answer.lower() == "pizza":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Which Australian marsupial enjoys eating eucalyptus leaves?\n")
if answer.lower() == "koala":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("In nautical terms, what is the opposite of port?\n")
if answer.lower() == "starboard":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions out of 5 correct")
print("You got " + str((score/5) * 100) + "% correct")
