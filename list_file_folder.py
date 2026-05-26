# list all the file in list of folders that user provides?

# identify module required to this program
import os 

# read input from the user  user give me 10 for example
folder_list = input("Please provide list of folder names with spaces in between:").split()

# for loop
# handle any known errors

for folders in folder_list:
   try:
     files = os.listdir(folders)
   except FileNotFoundError:
      print("===== please provide valif folder name, looks this folder does not exists:"+folders)
      break
   except PermissionError:
      print("no access to this folder:"+ folders)
      print("listing files for the folder -" + folders)
      print(files)

   for file in files:
      print(file)
