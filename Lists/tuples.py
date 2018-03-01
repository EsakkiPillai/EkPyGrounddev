# # Tuples are Similiar to the Lists but they are immutable it will throw an Error if we are going to append an item to it
# # tuples will be storing Hetegenous Items
# # Tuples are Immutable
#
# # Creating the Tuples
# val = "A", "B" , "C"
# t =("abc", "cat" , "eat")
# print(val)
# print(t)
#
# # check the Value Count in the Tuple
# print(len(val))
#
# greetings = ("Welcome to the", "Python", 3.64, "Programing")
# bad = ("bad company", "badCompany", 1974)
#
# # To Acess the Elements in the Tuples
# print("Printing the First Element from the Tuples bad is : {0}".format(bad[2]))
#
# # Out of Bound Exception
# # print("Printing the First Element from the Tuples bad is : {0}".format(bad[3]))
# # IndexError: tuple index out of range
#
# ###
# ## Print all the elements in the Tuples using While Loop
#
# for item in bad:
#     print ( " items in the Tuples are {0} ".format(item))
# count = 0
# while count < (len(greetings) ):
#     print ( " items in the Tuples are {0} ".format(greetings[count]))
#     count += 1
#
# # we cant change thhe values in the Tuples
#
# #bad[0]= "good"  # it will throw the exception as Follows
# #TypeError: 'tuple' object does not support item assignment
#
# # Immutable means wee cant change the content of the variables we can assign a new object of that type
#
# bad = bad[0], "GoodCompany", bad[2]
# print("*" * 50)
# print(bad)
# ## Here OPeraions are happened from  Right side
#
#
#
#
#
#
#
# ###########################
# # we assign Values to the Multiple Variables
# a = b = c = d =12
# print(c)
# print(b)
#
# # Assigning Multiple Values to the Multiple Variables
# a, b = 12 , 13
# print(b)
#
#
# # Variable Swap
#
# a, b = b, a
# print("a is now {0}".format(a))
# print("b is now {0}".format(b))
#
#
# # Assign Tuple Vales to the Variables
# # Unpacking the Tuples
# album = ("AR", 100, 2012)
# artist, songsCount, year = album
# print(artist)

# Tuples Containing Tuples

# imedla = "More Mayhem", "Imedla May", 2011, (
#     (1, "Song1"), (2, "Song2"), (3, "Song3"), (4, "Song4"))
# title, Artist, AlbumYear, tracks = imedla
# for track in tracks:
#     trackNUmber, song = track
#     print("{0} has released in {1} year and it has the Song {2}".format(title, AlbumYear,song))
#

# Tuples is Immutable , if the Tuple Contains a List its value can be changed as per the below Method
#
imedla1 = "More Mayhem", "Imedla May", 2011, (
    [(1, "Song1"), (2, "Song2"), (3, "Song3"), (4, "Song4")]
    )



imedla1[3].append((5,"Song5"))
print(imedla1)