# Takeaways
    #Conditions for execution (limiting the number of guesses)
    #Logic for feedback (too high/too low)
    #Restarting the game
    #And handling exceptions for bad numbers


def again():
    play_again = input("Do you wan to play again ? Y/N ")
    if play_again == "Y":
        play()
    else:
        print('Bye!')

import random as rd

def play():
    random = rd.randint(1,10)
    guesses= list()

    while len(guesses)<5:
        try:
            guess = int(input("Enter your guess: "))

        except ValueError:
            print("{} not a number".format(guess))
            print("Please try again")

        else:
            if guess == random:
                print('You got it ! My number was {}'.format(random))
                break
            else:
                if guess < random:
                    print("too low")
                else:
                    print("too high")

            guesses.append(guess)
    else:
        print("You didn't get it. My number was {}".format(random))
    again()

play()
