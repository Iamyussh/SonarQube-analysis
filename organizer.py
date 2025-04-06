import os
import shutil
from utils import get_extension_folder

def organize_folder(path):
    if not os.path.isdir(path):
        print("Error: Path does not exist.")
        return

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        if os.path.isfile(full_path):
            folder_name = get_extension_folder(filename)
            target_folder = os.path.join(path, folder_name)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(full_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} to {folder_name}/")

if __name__ == "__main__":
    folder_path = input("Enter folder path to organize: ")
    organize_folder(folder_path)
