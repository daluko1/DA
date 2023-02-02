import random
#user is prompted with instructions on how to play
print("Welcome to the first ever Guess The Number game!")
print("All you have to do is guess a number between the given set of values")
print("That's all there is to it. Good luck!")


#userGuess determines whether user guess is true
def userGuess(x):
    randomNum = random.randint(25, x)
    userGuess = 0

#create loop in order to make multiple guesses
    while userGuess != randomNum:
        userGuess = int(input(f"I am thinking of a number between 25 and {x}, take a guess: "))
        if userGuess > randomNum:
            print("Guess is too high, go again")
        elif userGuess < randomNum:
            print("Guess is too low, go again")
        else:
            print(f"You successfully guessed the number I was thinking of which was {randomNum}.")

userGuess(35)
