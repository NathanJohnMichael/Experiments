import random
random_number = random.randint (1, 10)

number_of_guesses = 0

while number_of_guesses < 10:

    number_of_guesses += 1

    guess = int(input("Guess a number between 1 and 10:"))

    if random_number == guess:
        print("You guessed it! The number was:", random_number)
        print("It took you", number_of_guesses, "guesses")
        break
    elif random_number > guess:
        print("Your guess is too low")
    elif random_number < guess:
        print("Your guess is too high")

if random_number != guess:
    print("Sorry, you didn't guess the number. The number was:", random_number)
else:
    print("The correct number was: ", random_number)