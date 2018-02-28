# print the numbers from 1 to 10 using For Loops
for i in range(1,10):
    print(" i is of now {0}".format(i))

# print the letters in the word
for i in "welcome to the python programming":
    print(i,"#",end=" ")

# clean the numbers

text = " 2,4578,45,.25,36eed4"
cleanedText=""
for i in range(0,len(text)):
    if text[i] in "0123456789":
        cleanedText=cleanedText+text[i]
finalText=int(cleanedText)
print("\nthe Final result is {0}".format(finalText) )

newcleanedtext=""
for char in text:
    if char in "0123456789":
        newcleanedtext= newcleanedtext + char

newfinaltext = int(newcleanedtext)
print("Final Text Value is {0}".format(newfinaltext))


# print 1 to 100 in multiples of 5
for i in range(0, 100, 20):
    print(" i is now {0} ".format(i))

# print a multiplication table up to 12

for i in range(1,16):
    for j in range(1,11):
        print(" {1} times {0} is {2}".format(i,j,i*j))
    print("----------------------------")
# print the items in the flipkart cart except a spam in the cart
cart= ["pen", "hpLaptop", "spam", "eggs", "pendrive", "spam"]

for item in cart:
    if item=="spam":
        continue
    print("item in the cart is {0}".format(item))

print("----------------------------------------------")

cart1= ["pen","hpLaptop","spam","eggs","pendrive","spam"]
# if a spam item is identified start the process
for item in cart1:
    if item =="spam":
        print("we are executing the break Protocol and the loop is ended ")
        break
    print("items in the cart is {0}".format(item))


# in python we are having for else
# if for loop is executed fully else block is executed
# if for loop is breaked then else block is skipped



##augmented Assignments rather tha long hand
# cleanedText = cleanedText + text[i]
# this can be replaced as
# cleanedText += text[i]














