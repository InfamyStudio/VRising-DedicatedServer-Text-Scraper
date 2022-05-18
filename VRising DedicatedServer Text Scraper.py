#By InfamyStudio - CortexCode - ~Cortex~
import os

path = "E:/SteamLibrary/steamapps/common/VRisingDedicatedServer/"
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

input("Press Enter To Exit...")
f.close()
