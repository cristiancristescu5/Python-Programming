import os
import sys


def rename_files(dir_path):
    index = 0
    try:
        if not os.path.isdir(dir_path):
            print(f"Directorul: {dir_path} nu exista")
            return
        for i, file in enumerate(os.listdir(dir_path)):
            try:
                base, extension = os.path.splitext(file)
                new_file = os.path.join(dir_path, f"file{index}{extension}")
                old_file = os.path.join(dir_path, file)
                os.rename(old_file, new_file)

            except Exception as e:
                print(f"Eroare: {str(e)}")
            index += 1
    except Exception as e:
        print(f"Eroare: {str(e)}")


rename_files("C:\\Users\\crist\\OneDrive\\Desktop\\New folder")
