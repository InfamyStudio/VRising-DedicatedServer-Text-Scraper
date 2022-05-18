#By InfamyStudio - CortexCode - ~Cortex~
import os
path = "E:/SteamLibrary/steamapps/common/VRisingDedicatedServer/"

def querySystem():
    filelist = []
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
        f.close()
    else:
        print("Total Files Containing Your Query '" + query + "': " + str(len(filelist)))
        f.close()

def searchAgain():
    while True:
        try:
            again = str(input("Would you like to search again? (y/n): ")).upper()
            if again == "Y":
                print("Restarting Search!")
                querySystem()
            elif again == "N":
                print("Exiting Search!")
                break
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input!")
if __name__ == "__main__":
    print("Please Make Sure To Change Your Path To Your Server Folder In The Code - Will Rework this later!")
    querySystem()
    searchAgain()


