# A Simple Example for While Loop
# availableDirection = [ 'East' , ' West' , 'NorthEast' , 'SouthWest']
# choseDirection=""
# while choseDirection not in availableDirection:
#     choseDirection = input("please enter the Direction")
#     if choseDirection == 'quit':
#         print("Game Over!!!! you have Quit")
#         break
#     if choseDirection == 'OneMoreTime':
#         print("Very Good")
#         continue
# else:
#     print("Finally You have printed the Correct Direction")

import random
highest = int(input(" please enter the highest Value...\n"))
answer = random.randint(1, highest)
guessCount = int(input("please enter how many guess u will take\n "))
guess = int(input("please Guess a Number between 1 and {0}\n".format(highest)))
count = 0
while count < guessCount:
    count += 1
    if guess != answer and (guessCount - count) > 0:
        if guess < answer:
            print("Please Guess Higher")
            print(" you have {0} More Chances to guess the Number".format(guessCount - count))
        else:
            print("Please Guess Lower")
            print(" you have {0} More Chances to guess the Number".format(guessCount - count))
        guess = int(input("please Guess the Number again\n"))
    elif guess == answer:
        print("you have guessed the Correct Number in {0} Times ".format(count))
        break
