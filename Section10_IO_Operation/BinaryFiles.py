###########################################
# Binary Files
##########################################

# We are going to store the Files in the Binary Format all we have to do is use "b" in the open method
# we have to convert the int and String into Bytes First before we save something into the Binary File Formats
# text mode - bw { b - binary and w for Write }
# Convert Data Types to Byes using bytes()
# binSampleObj.write(bytes([i])) - We have passed list as an Parameter  
## Example 1 : We r going to write a  one to 16 into a Binary File

with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\binarySampleFile",'bw') as binSampleObj:
    for i in range(1,17):
        binSampleObj.write(bytes([i]))

print("Reading the Same Binary File ...")
with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\binarySampleFile",'br') as binreadSampleObj:
    for b in binreadSampleObj:
        print(b)