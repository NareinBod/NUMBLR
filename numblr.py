#NUMBLR
import random

number = random.randint(1,100)
tries = 0
while tries < 6:
    choice = (input('Guess a number between 1 and 100: '))
    if (choice.isdigit() == False):
        print("Enter a valid number.")
    elif (1 <= int(choice) <= 100 ):
        tries += 1
        print(f"try {tries}: {choice}")
        if (choice == number):
            print("Congratulations! You've guessed the correct number.")
            break
        elif (int(choice) < number):
            print("Too Low!")
        elif (int(choice) > number):
            print("Too High!")
    else:
        print("Enter a number in the range of 1 to 100.")

print("Exceeded the number of tries. Please try again.")




       