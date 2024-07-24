import os
import shutil

LANGUAGES = ["Afrikaans", "English"] #TODO: 
OTHER = [ "Business Studies", "Computer Application Technology", "Geography", "Life Sciences", "Mathematical Literacy", "Mathematics", "Physical Sciences"] # TODO: "Accounting", 
FOLDER = r"C:\Users\rahil\OneDrive\Desktop\Coding\Python\Automation"

dir_list = os.listdir(FOLDER) 

for file_folder in dir_list:
    for subj in OTHER:
        os.chdir(f"{FOLDER}\{subj}") # main subj dir
        destination = 'EMPTY'
        source = f"{FOLDER}\{file_folder}"

        if ("Paper 1" in file_folder or "MS Office"in file_folder or "Memo 1" in file_folder or "P1" in file_folder) and subj in file_folder:
            os.chdir("Paper 1/Finals") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except:
                pass

        if ("Paper 2" in file_folder or "Memo 2" in file_folder or "P2" in file_folder) and subj in file_folder:
            os.chdir("Paper 2/Finals") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except:
                pass
        
        if ("Paper 3" in file_folder or "Memo 3" in file_folder or "P3" in file_folder) and subj in file_folder:
            os.chdir("Paper 1/Finals") #TODO
            new_destination = os.getcwd()
            try:
                cpy = shutil.copy(source, new_destination)
                print("Done copying")
            except Exception as e:
                print('ERROR ERROR ERROR ERROR ERROR', e)
            os.chdir(f"{FOLDER}\{subj}")

            os.chdir("Paper 2/Finals") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except:
                pass

    os.chdir(FOLDER)

    for subject in LANGUAGES:
        os.chdir(f"{FOLDER}\{subject}") # main subj dir
        destination = 'EMPTY'
        source = f"{FOLDER}\{file_folder}"

        if "P1" in file_folder and subject in file_folder:
            os.chdir("Paper 1/Finals") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except Exception as e:
                print("Paper 1", e)

        if "P2" in file_folder and subject in file_folder:
            os.chdir("Paper 2/Finals") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except Exception as e:
                print("Paper 2", e)            

        if "P3" in file_folder and subject in file_folder:
            os.chdir("Paper 3/Finals") # TODO
            destination = os.getcwd()
            try:
                dest = shutil.move(source, destination) 
            except Exception as e:
                print("Paper 3", e)

        os.chdir(FOLDER)

print("DONE")