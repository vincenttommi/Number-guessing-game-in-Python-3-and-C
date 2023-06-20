import random
import math

# Taking Inputs
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Generating a random number between the lower and upper bounds
x = random.randint(lower, upper)
print("\n\tYou have only",
      round(math.log(upper - lower + 1, 2)),
      "chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# For calculation of the minimum number of guesses depending on the range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Taking the guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print("Congratulations! You guessed it right in",
              count, "tries.")
        # Once guessed correctly, the loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If the number of guesses exceeds the required guesses, show this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
