import os
import sys


def count_extensions(dir_path):
    extensions = {}
    try:
        for path, dirs, files in os.walk(dir_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension in extensions:
                    extensions[extension] += 1
                else:
                    extensions[extension] = 1
    except Exception as e:
        print(f"Eroare: {e}")
        return
    return extensions


print(count_extensions(sys.argv[1]))
