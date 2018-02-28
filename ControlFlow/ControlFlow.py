#Chapter 06 Control Flow Vid 25 - 37
__author__="Esak"
# for loop
    # check a range of Numbers whether its odd or Even
    # please input an age and check whether the user can poll the vote or not
    # Guess a Number between 1 to 10 using if elif
#for i in range(1,100):
#    if (i%2 ==0):
#        print("Even Nos are {0:5}".format(i))
#    else:
#        print("check for another no")



age = int(input("please enter ur age "))
if not (age < 18):
    print("you are allowed to Vote")
else:
    print("Please come back {0} years ".format(18-age))


Src = "Welcome to Prgramming World"
destLetter = input("please enter the character to search for ")
if destLetter in Src:
    print(" the letter we are looking for is available in the src")
else:
    print(" Letter we are looking for is not available in the src ")

# in
# not in

