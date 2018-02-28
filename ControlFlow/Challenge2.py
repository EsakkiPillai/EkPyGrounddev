# users enter the ip address as input and we are going to findout the no of segments and no of characters in the segment

# ipaddress=input("please enter the IP address:- \t ")
# countItem=0
# value=ipaddress.split(".")
# for item in value:
#     if int(item) in range(0,256) and len(value) <=4:
#         countItem +=1
#         print(" {0} Section has the value as {1} and its length is {2}".format(countItem,item,len(item)))
#     else:
#         print("you have entered the wrong IP Address Format, PLease check it ")
#         break
# print("we have the Total Segments as {0}".format(countItem))
#
# ### Unlike Java we can acess the variable ITEM outside the for loop also
# ## which we dont usually do it Java
# # we need to make sure for loop executes at least only once so that we can get the value if the loop doesnt executed we get an exception
# #     to overcome it we usually asign the empty string to the chareacter


ipaddress = input("please enter an IP Address "
                  "seperated by :\n")

if ipaddress[-1] != ".":
    ipaddress += "."
segment_length = 0
segment = 1
for character in ipaddress:
    if character == '.':
        print("segment {0} contains {1} values".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
