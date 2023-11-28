import os
import sys


def compute_total_size(dir_path):
    count = 0
    try:
        for path, dirs, files in os.walk(dir_path):
            for f in files:
                g = os.path.join(path, f)
                count += os.path.getsize(g)
    except Exception as e:
        print(f"Eroare: {str(e)}")
    return count


print(f"Total size in {sys.argv[1]} is {compute_total_size(sys.argv[1])/8}")
