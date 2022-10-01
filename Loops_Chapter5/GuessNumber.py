import random

# Generate a random number to be guessed
number = random.randint(1, 150)
number = 123
starcount = 100

print("Guess a magic number between 0 and 150")

guess = -1
while guess != number:
    # Prompt the user to guess the number
    guess = eval(input("Enter your guess: "))

    if guess == number:
        print("Yes, the number is", number)
        print("You won 1,000 stars")
        starcount = starcount + 1000
        print("Your total star count is: " + str(starcount))
    elif guess > number:
        print("Your guess is too high")
        starcount = starcount - 10
    else:
        print("Your guess is too low")
        starcount = starcount - 10
