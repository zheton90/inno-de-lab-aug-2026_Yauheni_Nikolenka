import random

num = random.randint(1,20)
attempt = 0
isGuess = "false"

print("Guess of a number between 1 and 20")

while attempt < 5:
    yourNumb = int(input(f"{num} attempt. Enter a number between 1 and 20: "))
    if yourNumb == num:
        print("You guessed")
        break
    elif yourNumb > num:
        attempt += 1
        print(f"Too high. You have {5 - attempt} attempts")
    else:
        attempt += 1
        print(f"Too low. You have {5 - attempt} attempts")

if attempt == 5:
    print("You didn't guessed the correct number")
    