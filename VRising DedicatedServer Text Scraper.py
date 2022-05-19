#By InfamyStudio - CortexCode - ~Cortex~
import os
import sys

def validatePath(path):
    if os.path.exists(path):
        print("Your VRising Path Has Been Validated!")
    else:
        print("VRising Path Does Not Exist!")
        print("Deleting path.txt")
        os.remove("path.txt")
        print("Restarting Program!")
        checkPath()

def checkPath():
    try:
        f = open("path.txt","r")
        path = f.read()
        f.close()
        validatePath(path)
        querySystem(path)
    except FileNotFoundError:
        while True:
            print("My Path For Example: E:/SteamLibrary/steamapps/common/VRisingDedicatedServer/")
            path = input("Please Enter Your Path To VRising Dedicated Server: ")
            if path == "":
                print("Invalid Path")
            else:
                f = open("path.txt","w")
                f.write(path)
                f.close()
                break
        validatePath(path)
        querySystem(path)

def querySystem(path):
    filelist = []
    fileresult = []
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
                fileresult.append(name)
                print("In File: " + name + "\nFull Line String Was Mentioned: " + line + "Line Number: " + str(contents.index(line)))
            elif query.upper() in line:
                results = True
                fileresult.append(name)
                print("In File: " + name + "\nFull Line String Was Mentioned: " + line + "Line Number: " + str(contents.index(line)))
            elif query.lower() in line:
                results = True
                fileresult.append(name)
                print("In File: " + name + "\nFull Line String Was Mentioned: " + line + "Line Number: " + str(contents.index(line)))
            elif query.capitalize() in line:
                results = True
                fileresult.append(name)
                print("In File: " + name + "\nFull Line String Was Mentioned: " + line + "Line Number: " + str(contents.index(line)))
            elif query.title() in line:
                results = True
                fileresult.append(name)
                print("In File: " + name + "\nFull Line String Was Mentioned: " + line + "Line Number: " + str(contents.index(line)))

    if results == False:
        print("No Results With Search Query!")
        f.close()
        searchAgain(path)
    else:
        print("Total Files Containing Your Query '" + query + "': " + str(len(fileresult)))
        f.close()
        searchAgain(path)

def searchAgain(path):
    while True:
        try:
            again = str(input("Would you like to search again? (y/n): ")).upper()
            if again == "Y":
                print("Restarting Search!")
                querySystem(path)
            elif again == "N":
                print("Exiting VRising Text Scraper!")
                print("Made With Love By InfamyStudio~CortexCode")
                sys.exit()
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input!")

if __name__ == "__main__":
    path = checkPath()
    


