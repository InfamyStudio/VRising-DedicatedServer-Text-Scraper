#By InfamyStudio - CortexCode - ~Cortex~
import os

print("Please Make Sure To Change Your Path To Your Server Folder In The Code - Will Rework this later!")

path = "E:/SteamLibrary/steamapps/common/VRisingDedicatedServer/"
filelist = []
while True:
    query = str(input("Enter the text you want to search for: "))

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") or file.endswith(".log") or file.endswith(".json") or file.endswith(".info"):
                filelist.append(os.path.join(root,file))

    results = False
    for name in filelist:
        f = open(name, "r", encoding="utf8")
        contents = f.readlines()
        for line in contents:
            if query in line:
                results = True
                print("In File: " + name + "\nFull Line String Was Mentioned: " + line + "Line Number: " + str(contents.index(line)))

    if results == False:
        print("No Results With Search Query!")
    else:
        print("Total Files Containing Your Query '" + query + "': " + str(len(filelist)))

    again = str(input("Would you like to search again? (y/n): ")).upper()
    if again == "Y":
        print("Restarting Search!")
    if again == "N":
        print("Exiting Search!")
        f.close()
        break


