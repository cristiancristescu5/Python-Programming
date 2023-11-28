import os
import sys


def read_files_extension(dir_path, ext):
    try:
        if not os.path.isdir(dir_path):
            print(f"Directorul {dir_path} nu exista.")
            return

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(ext):
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            print(f.read())
                    except Exception as e:
                        print(f"Eroare:{str(e)}")
    except Exception as e:
        print(f"Eroare: {str(e)}")


read_files_extension(sys.argv[1], sys.argv[2])
