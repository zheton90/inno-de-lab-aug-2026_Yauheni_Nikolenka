import random

num = random.randint(1,20)
attempt = 1
isGuess = False

print("Guess of a number between 1 and 20")

while attempt <= 5:
    yourNumb = int(input(f"{attempt} attempt. Enter a number between 1 and 20: "))
    if yourNumb == num:
        print("You guessed")
        isGuess = True
        break
    elif yourNumb > num:
        attempt += 1
        if attempt <= 5:
            print(f"Too high. You have {6 - attempt} attempts")
    else:
        attempt += 1
        if attempt <= 5:
            print(f"Too low. You have {6 - attempt} attempts")

if not isGuess:
    print("You didn't guessed the correct number")
    