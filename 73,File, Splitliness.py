#File : Splitness

listmy = [1,2,3]

myfile = open("New file.txt","w")

for item in listmy:
    myfile.write(str(item)+ "\n")

myfile.close()

