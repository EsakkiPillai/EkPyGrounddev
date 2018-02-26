__author__ ="esak"

"""
 str(int ) will convert a  int into a String whereas in Java this conversion will happen automatically
   we can format in python and we can reuse them as many times we want 
"""
age = 24
print("esakki is " +str(age) +" years old")

# replacement Fields
print(" my marks are {0} in the maths".format(age))
#multiple Values
print("There are {0} days in the {1},{2},{3} of this calendar year".format(31,"Jan","Mar","may" ) )
# Using Triple Quotes
print("""
Jan : {0}
Feb :{1}
Mar :{0}
Apr :{2}
""".format(31,28,30))

#Python 2
## Using
print("My Age is %d Years" % age)
print(" My age is %d %s , %d %s thank u " %(age,"years",6,"Months"))

#a Simple For Loop
# i*i => i**2 => i power2
# i*i*i => i**3 =>  power 3

for i in range(1,12):
    print("No %d squared value is %4d and its cubed value is %d" %(i, (i*i),(i*i*i) ))

# to Format the Space we are going to use %2d
for i in range(1,12):
    print("No %2d squared value is %4d and its cubed value is %4d" %(i, i**2 , i**3 ))

# we are applying the same logic in Python 3 asbelow
for i in range(1,12):
    print("No {0:2} squared value is {1:4} and its cubed value is {2:6}" .format(i, i**2 , i**3 ))
    # if we want to left alignmented
    print("No {0:2} squared value is {1:<4} and its cubed value is {2:<6}" .format(i, i**2 , i**3 ))


#calculating the Pi value In Python2
print("PI value is Approximately is %12f"%(22/7))
print("PI value is Approximately is %12.50f"%(22/7))
#calculating the Pi value Python 3
print("PI value is Approximately is {0:12}".format(22/7))
print("PI value is Approximately is {0:12.50}".format(22/7))














