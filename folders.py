#! THIS IS TO MAKE THE FOLDERS
import os

LANGUAGES = ["Afrikaans ", "English"]
OTHER = ["Life Orientation"]
FOLDER = r"C:\Users\rahil\OneDrive\Desktop\Coding\Python\Automation"

# for subject in LANGUAGES:
#     os.mkdir(subject)
#     os.chdir(f"{subject}")

#     for x in range(1, 4):
#         os.mkdir(f"Paper {x}")
#         os.chdir(f"Paper {x}")
#         os.mkdir("Term 1")
#         os.mkdir("Term 2")
#         os.mkdir("Trials")
#         os.mkdir("Finals")
#         os.chdir("../")

#     os.chdir(FOLDER)

for subject in OTHER:
    os.mkdir(subject)
    os.chdir(f"{subject}")

    for x in range(1, 3):
        os.mkdir(f"Paper {x}")
        os.chdir(f"Paper {x}")
        os.mkdir("Term 1")
        os.mkdir("Term 2")
        os.mkdir("Trials")
        os.mkdir("Finals")
        os.chdir("../")

    os.chdir(FOLDER)


