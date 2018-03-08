# for Writing Purpose we use 'w'

wrestleMania = ["Wrestlemania1","Wrestlemania2","Wrestlemania3","Wrestlemania4","Wrestlemania5","Wrestlemania6","Wrestlemania7"]
with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\WWE",'w') as wweobj:
    for ele in wrestleMania:
        print(ele,file=wweobj,end= '#')
    
# if we want the buffer to Flush the data use flush = true

# Reading the Data
print("-"*30)
print("we are going to read the File")
print("-"*30)

with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\WWE",'r') as jober:
    for line in jober:
        print(line)


#Appending the Data into the Existing File
data = ["Hi","This" , "is", "a",  "Sample", "Text", "Message"]
with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\WWE",'a') as wweappendObj:
    for ele in data:
        print(ele,file=wweappendObj,end=' ')






