import random


def choserandom():
    return random.randint(1, 10)


def main():
    print("I am thinking of a number between 1 and 10.")
    print("You have 3 guesses left.")
    print("What's the number?")
    guessthisnumber = choserandom()
    for i in range(3):
        guess = int(input())
        if guess == guessthisnumber:
            print("Yes! You win!")
            break
        else:
            if guess > guessthisnumber:
                print(guess, "is too high.")
            else:
                print(guess, "is too low.")
            print("You have", 2-i, "guesses left.")
            if i == 2:
                print("You lose.")
                print("The number was", guessthisnumber)


main()
