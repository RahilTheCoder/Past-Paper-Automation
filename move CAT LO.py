import os
import shutil

OTHER = ["Computer Application Technology", "Life Orientation"]
FOLDER = r"C:\Users\rahil\OneDrive\Desktop\Coding\Python\Automation"

dir_list = os.listdir(FOLDER) 

for file_folder in dir_list:
    for subj in OTHER:
        os.chdir(f"{FOLDER}\{subj}") # main subj dir
        source = f"{FOLDER}\{file_folder}"
        check_1 = ("Paper 1" in file_folder or "Office"in file_folder or "Memo 1" in file_folder or "P1" in file_folder)
        
        if check_1 and subj in file_folder and "Nov" in file_folder:
            os.chdir("Paper 1/Finals") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except:
                pass
        elif check_1 and subj in file_folder and "May" in file_folder:
            os.chdir("Paper 1/Term 2") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except:
                pass
        elif check_1 and subj in file_folder and "Feb" in file_folder:
            os.chdir("Paper 1/Term 1") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except:
                pass

    os.chdir(FOLDER)

print("DONE")