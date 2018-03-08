# Print the Multiplication Table

with open("F:\\DevPlaySpace\\PythonPlayGround\\Workspace\\LEarnigProjects\\Helloworld\\Data\\Multiplier.txt","w") as muObj:
    for i in range(0,13):
        print(" {0} table".format(i),file=muObj)
        print("-" * 15,file=muObj)
        for j in range(1,11):
            print(" {0:>2} times {1} is {2}" .format(j,i,j*i), file=muObj,end=" ")
        print(file=muObj)
        print("*" * 45,file=muObj)


