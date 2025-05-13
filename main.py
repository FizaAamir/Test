# This script explains the contents of Folder1, Folder2, Folder3, and Folder4 in this project.

folders_info = {
    'Folder1': 'Contains folder1.py, which prints a hello message specific to folder 1.',
    'Folder2': 'Contains folder2.py, which prints a hello message specific to folder 2.',
    'Folder3': 'Contains folder3.py, which prints a hello message specific to folder 3.',
    'Folder4': 'Contains folder4.py, which (possibly by mistake) prints the same message as folder1.py, i.e., a hello message for folder 1.'
}

for folder, description in folders_info.items():
    print(f"{folder}: {description}\n")
