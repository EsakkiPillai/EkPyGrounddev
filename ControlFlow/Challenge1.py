# Write a small Program to ask for a name and age and check if the person age is the right age to go to 18-30 holiday
#they must be over 18 and under 31
# if they are welcome them to the holiday
# else refuse them

name= input("please enter your Name : ")
age = int(input(" Hi {0} ! please enter your age".format(name)))
if age > 31 :
    print(" you are too old to enter the Holiday ..")
elif (17 < age< 31):
    print("Please welcome to the Club")
else:
    print("please come back after {0} years".format(18-age))

