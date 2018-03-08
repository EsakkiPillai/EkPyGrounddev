# # to open the FIle
#

# readLine - reads the Files Line By Line and return as String
# readLines - Reads the entire file and load it into the Memory and return the values as List
# read

# jobber = open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\SampleTextFile",'r')
#
# for line in jobber:
#     if "he" in line:
#         print(line,end='')
#
# jobber.close()
#
# # if we fail to close the file , it may get corrupted  so more pythonic way to do that is

# implement the same using the With Statemnet

# with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\SampleTextFile",'r') as jobber:
#     for line in jobber:
#         if "he" in line:
#             print(line, end='$$$$')

# as per the Above statement we dont need to explicitly close the file as with statement automatically Close it


# with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\SampleTextFile",'r') as jobber:
#     line = jobber.readline()
#     while line:
#         print(line,end='#')
#         line=jobber.readline()

# jobber.readLines() will fetch the entire File into it
#
# with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\SampleTextFile",'r') as jobber:
#     lines = jobber.readlines()
# print(lines)
#
# # these Results in a list and we can Process the List further
#
# for ele in lines:
#     print(ele)