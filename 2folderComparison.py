#compare the contents of two folders and return their differences. (non-recursive) Made to check copies and backups. 

import os,re
from tkinter.filedialog import askdirectory
path1=askdirectory(title="Dir1: Folder path that has all the files you want to check")
path2=askdirectory(title="Dir2: Folder path to check if it has all the files in Dir1:")    #larger dir
excludePrompt=int(input("Exclude any files types? 0: .ndpi, 1:.vsi, 9: Do not exclude any.:"))
if excludePrompt==0:
    excludetype="ndpi"
elif excludePrompt==1:
    excludetype="vsi"
else:
    excludetype="NOWAYTHISISGONNAMATCH"
print("Excluding file names that have:"+excludetype)
def compareDirs(path1,path2):           #checks if everything in path1 is in path2. outputs the list of extra files and the list of extra dirs in path1 as a tuple)
    extrafile=[]
    extradir=[]
    for f in os.listdir(path1):  #iterate smaller dir to see if the larger dir contains all of them
        if excludetype not in f:
            filePath=os.path.join(path1, f)
            matchflag=False
            for i in os.listdir(path2):
                if f in i :
                    matchflag=True
            if matchflag==False:
                if os.path.isfile(filePath):
                    extrafile.append(f)
                else:
                    extradir.append(f)
    return(extrafile,extradir)

print(f"Checking overlap between Dir1: \"{path1}\" and Dir2: \"{path2}\".")

extrafile1,extradir1=compareDirs(path1,path2)
extrafile2,extradir2=compareDirs(path2,path1)
pattern=r"^.*\/(.*)"
path1Short=re.match(pattern=pattern,string=path1)
path1Short=path1Short.group(1)
path2Short=re.match(pattern=pattern,string=path2)
path2Short=path2Short.group(1)

spaceLen=max(len(path1Short),len(path2Short))
diff=max(len(path1Short),len(path2Short))-min(len(path1Short),len(path2Short))
space=" "
for i in range(0,spaceLen):
    space=space+" "
dirFlag=False
fileFlag=False
print("--------------------------------------------------------------------------------------")
print(f"\n{space}Extra Folders\tExtra Files")
print("\n--------------------------------------------------------------------------------------")
print(f"\n\"{path1Short}\"{space[0:(len(space)-len(path1Short))]}{len(extradir1)}{space[0:17]}{len(extrafile1)}")
print(f"\n\"{path2Short}\"{space[0:(len(space)-len(path2Short))]}{len(extradir2)}{space[0:17]}{len(extrafile2)}")
print("\n--------------------------------------------------------------------------------------")

detailsFlag=input(f"Show details of the difference between folders? 0: show list of extra files in both folders, 1: show list of extra files in \"{path1Short}\", 2: show list of extra files in \"{path2Short}\", 9: Skip.:")
detailsFlag=int(detailsFlag)
while not detailsFlag in (0,1,2,9):
    print("Invalide input. Please input 0,1,2,or 9.")
    detailsFlag=input(f"Show details of the difference between folders? 0: show list of extra files in both folders, 1: show list of extra files in \"{path1Short}\", 2: show list of extra files in \"{path2Short}\", 9: Skip.:")
    detailsFlag=int(detailsFlag)
if detailsFlag==0:
    print("--------------------------------------------------------------------------------------")
    print(f"\nExtra Files in {path1Short}:")
    for i in range(1,(len(extrafile1)+1)):
        print(f"{i}. {extrafile1[i-1]}")
    print(f"\nExtra folders in {path1Short}:")
    for i in range (1,(len(extradir1)+1)):
        print(f"{i}. {extradir1[i-1]}")
    print("\n--------------------------------------------------------------------------------------")
    print(f"\nExtra Files in {path2Short}:")
    for i in range(1,(len(extrafile2)+1)):
        print(f"{i}. {extrafile2[i-1]}")
    print(f"\nExtra folders in {path2Short}:")
    for i in range (1,(len(extradir2)+1)):
        print(f"{i}. {extradir2[i-1]}")
elif detailsFlag==1:
    print("--------------------------------------------------------------------------------------")
    print(f"\nExtra Files in {path1Short}:")
    for i in range(1,(len(extrafile1)+1)):
        print(f"{i}. {extrafile1[i-1]}")
    print(f"\nExtra folders in {path1Short}:")
    for i in range (1,(len(extradir1)+1)):
        print(f"{i}. {extradir1[i-1]}")
    print("\n--------------------------------------------------------------------------------------")
elif detailsFlag==2:
    print("--------------------------------------------------------------------------------------")
    print(f"\nExtra Files in {path2Short}:")
    for i in range(1,(len(extrafile2)+1)):
        print(f"{i}. {extrafile2[i-1]}")
    print(f"\nExtra folders in {path2Short}:")
    for i in range (1,(len(extradir2)+1)):
        print(f"{i}. {extradir2[i-1]}")
    print("\n--------------------------------------------------------------------------------------")
